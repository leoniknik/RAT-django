from django.conf.urls import url
from api.views import signin, signup, edit_user, add_vehicle, edit_vehicle, get_list_of_actual_crashes,\
    get_list_of_history_crashes, get_list_of_offers, get_list_of_vehicles, get_service, get_service_reviews,\
    get_lists_of_vehicles_and_crashes, get_lists_of_offers_and_services, get_lists_of_high_low_offers_and_services,\
    delete_vehicle,update_high_offer,update_low_offer
urlpatterns = [
    url(r'^signin$', signin),  # POST
    url(r'^signup$', signup),  # POST
    url(r'^edit_user$', edit_user),  # POST
    url(r'^add_vehicle$', add_vehicle),  # POST
    url(r'^edit_vehicle$', edit_vehicle),  # POST
    url(r'^get_list_of_actual_crashes$', get_list_of_actual_crashes),  # GET
    url(r'^get_list_of_history_crashes$', get_list_of_history_crashes),  # GET
    url(r'^get_list_of_offers$', get_list_of_offers),  # GET
    url(r'^get_list_of_vehicles$', get_list_of_vehicles),  # GET
    url(r'^get_service$', get_service),  # GET
    url(r'^get_service_reviews$', get_service_reviews),  # GET
    url(r'^get_lists_of_vehicles_and_crashes$', get_lists_of_vehicles_and_crashes), # GET
    url(r'^get_lists_of_offers_and_services$', get_lists_of_offers_and_services), # GET
    url(r'^get_lists_of_high_low_offers_and_services$', get_lists_of_high_low_offers_and_services),  # GET
    url(r'^delete_vehicle$', delete_vehicle),  # GET
    url(r'^update_high_offer$', update_high_offer),  # GET
    url(r'^update_low_offer$', update_low_offer),  # GET
]
