from django.conf.urls import url
from api.views import signin, signup, edit_user


urlpatterns = [
    url(r'^signin$', signin),
    url(r'^signup$', signup),
    url(r'^edit_user$', edit_user),
]
