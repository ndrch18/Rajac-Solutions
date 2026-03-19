from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from system_app.models import Account, RawMaterial
from .forms import RawMaterialForm
from .models import MaterialUnit

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from urllib.parse import urlencode

#Global variable for login authentication
account_id = 0

# Function for login page
def login_view(request):
    message = request.session.pop('message', '')

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')

        try:
            account = Account.objects.get(employee_id=employee_id, password=password)
            if password == account.password:
                request.session['account_id'] = account.id
                request.session['employee_id'] = account.employee_id

                # Route based on the first character of the employee ID
                if employee_id.startswith('0'):
                    return redirect('owner_homepage')
                elif employee_id.startswith('1'):
                    return redirect('prodman_homepage')
                else:
                    message = "Unrecognized account type. Please contact your administrator."
            else:
                message = "Invalid login. Please check your username or password."
        except Account.DoesNotExist:
            message = "Invalid login. Please check your username or password."

    return render(request, 'system_app/login.html', {'message': message})

def logout_view(request):
    request.session.pop('account_id', None) 
    return redirect('login')

def change_password_view(request):
    # must be logged in
    account_id = request.session.get('account_id')
    if not account_id:
        return redirect('login')

    message = ""

    if request.method == "POST":
        current_pw = request.POST.get("current_password")
        new_pw = request.POST.get("new_password")
        confirm_pw = request.POST.get("confirm_password")

        account = Account.objects.get(id=account_id)

        if current_pw != account.password:
            message = "Current password is incorrect."
        elif not new_pw:
            message = "New password cannot be empty."
        elif new_pw != confirm_pw:
            message = "New passwords do not match."
        else:
            account.password = new_pw
            account.save()
            message = "Password changed successfully!"

    return render(request, "system_app/change_password.html", {"message": message})


def owner_homepage(request):
    if not request.session.get('account_id'):
        return redirect('login')
    # Enforce role: owner IDs start with '0'
    employee_id = request.session.get('employee_id', '')
    if not employee_id.startswith('0'):
        return redirect('login')
    return render(request, 'system_app/owner_home.html', {
        'employee_id': employee_id,
    })

def prodman_homepage(request):
    if not request.session.get('account_id'):
        return redirect('login')
    employee_id = request.session.get('employee_id', '')
    if not employee_id.startswith('1'):
        return redirect('login')
    return render(request, 'system_app/prodman_home.html', {
        'employee_id': employee_id,
    })

def prodman_matinv(request):
    # Protect page
    if not request.session.get('account_id'):
        return redirect('login')

    # -------------------------
    # GET FILTERS
    # -------------------------
    if not request.session.get('account_id'):
        return redirect('login')

    q = (request.GET.get('q') or "").strip()
    category = (request.GET.get('category') or "all").strip()
    sort = (request.GET.get('sort') or "alpha").strip()  # default A–Z

    qs = RawMaterial.objects.all()

    # Category filter (skip if "all")
    if category in {"fabrics", "trims", "accessories"}:
        qs = qs.filter(material_category=category)

    # Search filter
    if q:
        qs = qs.filter(material_name__icontains=q)

    # Sorting
    if sort == "highest":
        qs = qs.order_by("-material_quantity", "material_name")
    elif sort == "lowest":
        qs = qs.order_by("material_quantity", "material_name")
    elif sort == "alpha_desc":
        qs = qs.order_by("-material_name")
    else:
        qs = qs.order_by("material_name")  # A–Z

    # -------------------------
    # HANDLE MODAL POST
    # -------------------------
    if request.method == "POST":
        form = RawMaterialForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.full_clean()  # runs your RawMaterial.clean()
            obj.save()

            # Preserve filters on redirect
            params = {}
            if category:
                params["category"] = category
            if q:
                params["q"] = q

            url = reverse("prodman_matinv")
            if params:
                url = f"{url}?{urlencode(params)}"

            return redirect(url)

    else:
        form = RawMaterialForm()

    # -------------------------
    # BUILD UNIT MAP FOR JS
    # -------------------------
    units_by_category = {
        "fabrics": [
            {"id": u.id, "name": u.unit_name}
            for u in MaterialUnit.objects.filter(category="fabrics").order_by("unit_name")
        ],
        "trims": [
            {"id": u.id, "name": u.unit_name}
            for u in MaterialUnit.objects.filter(category="trims").order_by("unit_name")
        ],
        "accessories": [
            {"id": u.id, "name": u.unit_name}
            for u in MaterialUnit.objects.filter(category="accessories").order_by("unit_name")
        ],
    }

    # -------------------------
    #EDIT MODEL SUPPORT
    # -------------------------
    edit_id = request.GET.get("edit")
    edit_target = None
    edit_form = None

    if edit_id:
        try:
            edit_target = RawMaterial.objects.get(pk=int(edit_id))
            edit_form = RawMaterialForm(instance=edit_target)
        except (RawMaterial.DoesNotExist, ValueError):
            edit_target = None
            edit_form = None

    # -------------------------
    # CONTEXT
    # -------------------------
    context = {
        "materials": qs,
        "selected_category": category,
        "q": q,
        "sort": sort,
        "as_of": timezone.localtime(timezone.now()),
        "category_choices": [
            ("all", "All"),
            ("fabrics", "Fabrics"),
            ("trims", "Trims"),
            ("accessories", "Accessories"),
        ],
        "form": form,
        "units_by_category_json": json.dumps(units_by_category, cls=DjangoJSONEncoder),
        "edit_target": edit_target,
        "edit_form": edit_form,
        "open_edit": bool(edit_target),
    }

    return render(request, "system_app/prodman_matinv.html", context)
    
def edit_raw_material(request, pk):
    if not request.session.get('account_id'):
        return redirect('login')

    material = get_object_or_404(RawMaterial, pk=pk)

    # Preserve current filters when redirecting back
    q = (request.GET.get("q") or "").strip()
    category = (request.GET.get("category") or "all").strip()
    sort = (request.GET.get("sort") or "alpha").strip()

    if request.method == "POST":
        form = RawMaterialForm(request.POST, instance=material)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.full_clean()
            obj.save()

            params = {}
            if category:
                params["category"] = category
            if q:
                params["q"] = q
            if sort:
                params["sort"] = sort

            url = reverse("prodman_matinv")
            if params:
                url = f"{url}?{urlencode(params)}"
            return redirect(url)

    # If someone visits edit URL directly (GET), just bounce back and open modal
    params = {"edit": pk}
    if category:
        params["category"] = category
    if q:
        params["q"] = q
    if sort:
        params["sort"] = sort

    url = reverse("prodman_matinv")
    return redirect(f"{url}?{urlencode(params)}")

def delete_raw_material(request, pk):
    if not request.session.get('account_id'):
        return redirect('login')

    material = get_object_or_404(RawMaterial, pk=pk)

    # Preserve filters from URL
    q = (request.GET.get("q") or "").strip()
    category = (request.GET.get("category") or "all").strip()
    sort = (request.GET.get("sort") or "alpha").strip()

    if request.method == "POST":
        material.delete()

    # Build redirect URL with preserved params
    params = {}
    if category:
        params["category"] = category
    if q:
        params["q"] = q
    if sort:
        params["sort"] = sort

    url = reverse("prodman_matinv")
    if params:
        url = f"{url}?{urlencode(params)}"

    return redirect(url)