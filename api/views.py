from RATapp.models import User, Vehicle, Crash, CrashDescription, Offer, Service, Review,HighOffer,LowOffer
from authorization import Auth
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core import serializers


def signin(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        user = Auth().authenticate(email, password)
        if user is None:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0, "data": {"user_id": user.id, "email": user.email,
                                                     "firstname": user.firstname, "lastname": user.lastname,
                                                     "phone": user.phone}})
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
        return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def add_vehicle(request):
    try:
        user_id = request.POST['user_id']
        VIN = request.POST['VIN']
        number = request.POST['number']
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        vehicle = Vehicle.create_vehicle(VIN, number, brand, model, year, user_id)
        return JsonResponse({"code": 0,"data":{"vehicle_id":vehicle.id}})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def edit_vehicle(request):
    try:
        vehicle_id = request.POST['vehicle_id']
        VIN = request.POST['VIN']
        number = request.POST['number']
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        is_auction = request.POST['is_auction']
        Vehicle.update_vehicle(vehicle_id, VIN, number, brand, model, year,is_auction)
        return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})

def delete_vehicle(request):
    try:
        vehicle_id = request.POST['vehicle_id']
        Vehicle.delete_vehicle(vehicle_id)
        return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})

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
        actual_crashes = Crash.objects.all().filter(actual=True, vehicle=vehicle).values('id', 'description__code',
                                                                                         'description__full_description',
                                                                                         'description__short_description',
                                                                                         'date', 'actual')
        data = list(actual_crashes)
        return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_list_of_history_crashes(request):
    try:
        vehicle_id = request.GET['vehicle_id']
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        history_crashes = Crash.objects.all().filter(actual=False, vehicle=vehicle).values('id', 'description__code',
                                                                                           'description__full_description',
                                                                                           'description__short_description',                                                                                       'date', 'actual')
        data = list(history_crashes)
        return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_list_of_offers(request):
    try:
        crash_id = request.GET['crash_id']
        crash = Crash.objects.get(pk=crash_id)
        offers = Offer.objects.all().filter(crash=crash).values('id','price','message', 'service__name', 'service_id')
        data = list(offers)
        return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_service(request):
    try:
        service_id = request.GET['service_id']
        service = Service.objects.get(pk=service_id)
        return JsonResponse({"code": 0, "data": service})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_service_reviews(request):
    try:
        service_id = request.GET['service_id']
        service = Service.objects.get(pk=service_id)
        reviews = Review.objects.all().filter(service=service)
        data = list(reviews)
        return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_lists_of_vehicles_and_crashes(request):
    try:
        user_id = request.GET["user_id"]
        user = User.objects.get(pk=user_id)
        vehicles = Vehicle.objects.filter(user=user).values('id', 'VIN', 'number', 'brand', 'model', 'year')
        vehicles = list(vehicles)
        for vehicle in vehicles:
            crashes = Crash.objects.filter(vehicle_id=vehicle["id"]).values('id', 'description__code', 'description__full_description',
                                            'description__short_description', 'date', 'vehicle_id', 'actual')
            crashes=list(crashes)
            vehicle['crashes'] = crashes
        return JsonResponse({"code": 0, "data": vehicles})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_lists_of_offers_and_services(request):
    try:
        user_id = request.GET["user_id"]
        vehicle_id = request.GET["vehicle_id"]
        user = User.objects.get(pk=user_id)
        vehicles = Vehicle.objects.filter(user=user,id=vehicle_id)
        offers = []
        for vehicle in vehicles:
            tmp_offers = Offer.objects.filter(vehicle=vehicle).values('id','vehicle_id','service_id','price','message','date','is_avalible','is_confirmed')
            for tmp_offer in tmp_offers:
                service = Service.objects.filter(id=tmp_offer['service_id']).values('id','name','description','address','phone','email')[0]
                reviews = Review.objects.filter(service_id=service["id"]).values('id','date','text','user_id')
                reviews_list=[]
                for review in reviews:
                    user = User.objects.filter(id = review['user_id']).values('id','firstname','lastname')[0]
                    review['user_id'] = user['id']
                    review['firstname'] = user['firstname']
                    review['lastname'] = user['lastname']
                    reviews_list.append(review)
                    service['reviews']=reviews_list
                    sl = []
                    sl.append(service)
                    service_list = list(sl)
                    tmp_offer_list=(tmp_offer)
                    tmp_offer_list['service']=service_list
                    offers.append(tmp_offer_list)
        return JsonResponse({"code": 0, "data": offers})
    except Exception as e:
        print(e)
    return JsonResponse({"code": 1})


def get_lists_of_high_low_offers_and_services(request):
    try:
        user_id = request.GET["user_id"]
        vehicle_id = request.GET["vehicle_id"]
        user = User.objects.get(pk=user_id)
        vehicles = Vehicle.objects.filter(user=user,id=vehicle_id)
        offers = []
        for vehicle in vehicles:
            tmp_high_offers = HighOffer.objects.filter(vehicle=vehicle).values('id','vehicle_id','service_id','price','message','date','is_avalible','is_confirmed')
            for tmp_high_offer in tmp_high_offers:
                tmp_low_offers = LowOffer.objects.filter(high_offer_id=tmp_high_offer['id']).values('id','crash_id','message','price','is_avalible','is_chosen')
                low_offers = list(tmp_low_offers)
                tmp_high_offer['low_offers'] = low_offers
                service = Service.objects.filter(id=tmp_high_offer['service_id']).values('id','name','description','address','phone','email')[0]
                reviews = Review.objects.filter(service_id=service["id"]).values('id','date','text','user_id')
                reviews_list=[]
                for review in reviews:
                    user = User.objects.filter(id = review['user_id']).values('id','firstname','lastname')[0]
                    review['user_id'] = user['id']
                    review['firstname'] = user['firstname']
                    review['lastname'] = user['lastname']
                    reviews_list.append(review)
                service['reviews']=reviews_list
                sl = []
                sl.append(service)
                service_list = list(sl)
                tmp_offer_list=(tmp_high_offer)
                tmp_offer_list['service']=service_list
                offers.append(tmp_offer_list)
        return JsonResponse({"code": 0, "data": offers})
    except Exception as e:
        print(e)
    return JsonResponse({"code": 1})