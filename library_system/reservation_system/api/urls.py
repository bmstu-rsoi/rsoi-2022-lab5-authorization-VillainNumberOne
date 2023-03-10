from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/reservations/(?P<username>.+)$', views.get_user_reservations),
    re_path(r'^api/v1/reservations/(?P<username>.+)/rented$', views.get_rented),
    re_path(r'^api/v1/reservation$', views.reservation),
]