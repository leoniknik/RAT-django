from django.shortcuts import render
from RATapp.models import User


def home(request):
    return render(request, 'main.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']

        if password != repeat_password:
            return render(request, 'signup.html')
        else:
            try:
                User.objects.create_user(email, password, firstname, lastname, phone)
                return render(request, 'signin.html')
            except Exception as e:
                print(e)
                return render(request, 'signup.html')
