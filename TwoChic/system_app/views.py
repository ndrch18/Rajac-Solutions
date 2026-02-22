from django.shortcuts import render, redirect
from django.utils import timezone
from system_app.models import Account, RawMaterial

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
                return redirect('prodman_homepage')
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


def prodman_homepage(request):
    if not request.session.get('account_id'):
        return redirect('login')

    return render(request, 'system_app/prodman_home.html')

def prodman_matinv(request):
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
    }
    return render(request, "system_app/prodman_matinv.html", context)
    
