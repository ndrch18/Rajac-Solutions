from django.shortcuts import render, redirect
from system_app.models import Account, RawMaterial

#Global variable for login authentication
account_id = 0

# Function for login page
def login_view(request):
    global account_id
    message = request.session.pop('message', '')
    if request.method == 'POST':
        username = request.POST.get('employee_id')
        password = request.POST.get('password')
        try:
            account = Account.objects.get(username=username, password=password)
            if password == account.password:
                account_id = account.id
                return redirect('view_employee')
            else:
                message = "Invalid login. Please check your username or password."
        except Account.DoesNotExist:
            message = "Invalid login. Please check your username or password."
    return render(request, 'system_app/login.html', {'message': message, 'account_id':account_id})


def hello_world(request):
    return render(request, 'system_app/hello_world.html')