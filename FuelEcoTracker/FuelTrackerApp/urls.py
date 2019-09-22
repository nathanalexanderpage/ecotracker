from django.urls import path

from . import views

# app_name = 'FuelTrackerApp'
urlpatterns = [
    # INDEX PATTERN
    # ex: /
    path('', views.eco_index, name='eco_index'),

    # AUTH PATTERN
    # ex: /auth/login/
    path('login/', views.user_login, name='user_login'),
    # ex: /auth/logout/
    path('logout/', views.user_logout, name='user_logout'),
    # ex: /auth/signup/
    path('signup/', views.user_signup, name='user_signup'),

    # STATION PATTERN
    # ex: /stations/
    path('stations/', views.fuel_station_index, name='fuel_station_index'),
    # ex: /stations/new/
    path('stations/new/', views.fuel_station_new, name='fuel_station_new'),
    # ex: /stations/5/
    path('stations/<int:fuel_station_id>/', views.fuel_station_detail, name='fuel_station_detail'),

    # PURCHASE PATTERN
    # ex: /fillups/
    path('fillups/', views.receipt_index, name='receipt_index'),
    # ex: /fillups/new/
    path('fillups/new/', views.receipt_new, name='receipt_new'),
    # ex: /fillups/3/
    path('fillups/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),

    # VEHICLE PATTERN
    # ex: /vehicles/
    path('vehicles/', views.vehicle_index, name='vehicle_index'),
    # ex: /vehicles/new/
    path('vehicles/new/', views.vehicle_new, name='vehicle_new'),
    # ex: /vehicles/4/
    path('vehicles/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]
