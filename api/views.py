from django.shortcuts import render
from RATapp.models import User
from authorization import Auth


def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = Auth().authenticate(email, password)
    if user is None:
        return None
    else:
        return render(request, "temp.html")


def signup(request):
    email = request.POST['email']
    password = request.POST['password']
    repeat_password = request.POST['repeat_password']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']

    if password != repeat_password:
        return None
    else:
        try:
            User.objects.create_user(email, password, firstname, lastname, phone)
            return render(request, 'signin.html')
        except Exception as e:
            print(e)
            return None
