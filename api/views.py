from RATapp.models import User, Vehicle, Crash, CrashDescription, Offer, Service, Review
from authorization import Auth
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core import serializers


def signin(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        user = Auth().authenticate(email, password)
        if user is None:
            return HttpResponseForbidden()
        else:
            return JsonResponse({"code": 0, "data": {"user_id": user.id}})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def signup(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        User.objects.create_user(email, password, firstname, lastname, phone)
        return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def edit_user(request):
    try:
        user_id = request.POST['user_id']
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        User.objects.update_user(user_id, email, password, firstname, lastname, phone)
        return JsonResponse({})
    except Exception as e:
        print(e)
        return JsonResponse({})


def add_vehicle(request):
    try:
        user_id = request.POST['user_id']
        VIN = request.POST['VIN']
        number = request.POST['number']
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        Vehicle.create_vehicle(VIN, number, brand, model, year, user_id)
        return JsonResponse({})
    except Exception as e:
        print(e)
        return JsonResponse({})


def edit_vehicle(request):
    try:
        vehicle_id = request.POST['vehicle_id']
        VIN = request.POST['VIN']
        number = request.POST['number']
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        Vehicle.update_vehicle(vehicle_id, VIN, number, brand, model, year)
        return JsonResponse({})
    except Exception as e:
        print(e)
        return JsonResponse({})


def get_list_of_vehicles(request):
    try:
        user_id = request.GET["user_id"]
        user = User.objects.get(pk=user_id)
        vehicles = Vehicle.objects.all().filter(user=user).values('id', 'VIN', 'number', 'brand', 'model', 'year')
        data = list(vehicles)
        return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_list_of_actual_crashes(request):
    try:
        vehicle_id = request.GET['vehicle_id']
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        actual_crashes = Crash.objects.all().filter(actual=True, vehicle=vehicle).values('id', 'description__code', 'description__full_description', 'description__short_description', 'date')
        data = list(actual_crashes)
        return JsonResponse({"data": data})
    except Exception as e:
        print(e)
        return JsonResponse({})


def get_list_of_history_crashes(request):
    try:
        vehicle_id = request.GET['vehicle_id']
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        history_crashes = Crash.objects.all().filter(actual=False, vehicle=vehicle).values('id', 'description__code', 'description__full_description', 'description__short_description', 'date')
        data = list(history_crashes)
        return JsonResponse({"data": data})
    except Exception as e:
        print(e)
        return JsonResponse({})


def get_list_of_offers(request):
    try:
        crash_id = request.GET['crash_id']
        crash = Crash.objects.get(pk=crash_id)
        offers = Offer.objects.all().filter(crash=crash)
        data = list(offers)
        return JsonResponse({"data": data})
    except Exception as e:
        print(e)
        return JsonResponse({})


def get_service(request):
    try:
        service_id = request.GET['service_id']
        service = Service.objects.get(pk=service_id)
        return JsonResponse(service)
    except Exception as e:
        print(e)
        return JsonResponse({})


def get_service_reviews(request):
    try:
        service_id = request.GET['service_id']
        service = Service.objects.get(pk=service_id)
        reviews = Review.objects.all().filter(service=service)
        data = list(reviews)
        return JsonResponse({"data": data})
    except Exception as e:
        print(e)
        return JsonResponse({})
