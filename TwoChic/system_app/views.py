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


def prodman_homepage(request):
    if not request.session.get('account_id'):
        return redirect('login')

    return render(request, 'system_app/prodman_home.html')

def prodman_matinv(request):
    # Optional: protect page using your session login
    if not request.session.get('account_id'):
        return redirect('login')

    # GET filters
    q = (request.GET.get('q') or "").strip()
    category = (request.GET.get('category') or "fabrics").strip()

    qs = RawMaterial.objects.all()

    if category in {"fabrics", "trims", "accessories"}:
        qs = qs.filter(material_category=category)

    if q:
        qs = qs.filter(material_name__icontains=q)

    qs = qs.order_by("material_name")

    context = {
        "materials": qs,
        "selected_category": category,
        "q": q,
        "as_of": timezone.localtime(timezone.now()),
        "category_choices": [
            ("fabrics", "Fabrics"),
            ("trims", "Trims"),
            ("accessories", "Accessories"),
        ],
    }
    return render(request, "system_app/prodman_matinv.html", context)
    
