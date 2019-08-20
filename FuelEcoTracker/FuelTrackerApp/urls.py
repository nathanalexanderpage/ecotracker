from django.urls import path

from . import views

urlpatterns = [
    # INDEX PATTERN
    # ex: /
    path('', views.index, name='index'),

    # AUTH PATTERN
    # ex: /auth/login/
    path('login/', views.login, name='login'),
    # ex: /auth/signup/
    path('signup/', views.signup, name='signup'),

    # STATION PATTERN
    # ex: /stations/
    path('stations/', views.fuel_station_index, name='receipt_index'),
    # ex: /stations/new/
    path('stations/new/', views.fuel_station_new, name='fuel_station_new'),
    # ex: /stations/5/
    path('stations/<int:fuel_station_id>/', views.fuel_station_detail, name='fuel_station_detail'),

    # PURCHASE PATTERN
    # ex: /purchases/
    path('purchases/', views.receipt_index, name='receipt_index'),
    # ex: /purchases/new/
    path('purchases/new/', views.receipt_new, name='receipt_new'),
    # ex: /purchases/3/
    path('purchases/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),

    # VEHICLE PATTERN
    # ex: /vehicles/
    path('purchases/', views.receipt_index, name='vehicle_index'),
    # ex: /vehicles/new/
    path('vehicles/new/', views.vehicle_new, name='vehicle_new'),
    # ex: /vehicles/4/
    path('vehicles/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]
