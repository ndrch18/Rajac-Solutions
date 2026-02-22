from django.shortcuts import render, redirect
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


    
