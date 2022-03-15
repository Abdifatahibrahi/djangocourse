from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="all-meetups"),
    path('<slug:meetup_slug>/success', views.confirm_registration, name="confirm-registration"),
    path('<slug:meetup_slug>', views.meetup_details, name="meetup-details")
] 