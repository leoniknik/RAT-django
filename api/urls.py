from django.conf.urls import url
from api.views import signin, signup


urlpatterns = [
    url(r'^signin/$', signin),
    url(r'^signup/$', signup),
]