from RATapp.models import User
from authorization import Auth
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest


def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = Auth().authenticate(email, password)
    if user is None:
        return HttpResponseForbidden()
    else:
        return JsonResponse({'user_id': user.id})


def signup(request):
    email = request.POST['email']
    password = request.POST['password']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']
    try:
        User.objects.create_user(email, password, firstname, lastname, phone)
        return HttpResponse()
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()


def edit_user(request):
    user_id = request.POST['user_id']
    email = request.POST['email']
    password = request.POST['password']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']
    try:
        User.objects.update_user(user_id, email, password, firstname, lastname, phone)
        return HttpResponse()
    except Exception as e:
        print(e)
        HttpResponseBadRequest()


def add_vehicle(request):
    pass


def edit_vehicle(request):
    pass


def list_of_vehicles(request):
    pass


def list_of_actual_crashes(request):
    pass


def list_of_history_crashes(request):
    pass


def description_of_crash(request):
    pass


def list_of_offers(request):
    pass
