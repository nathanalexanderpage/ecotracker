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
    # ex: /station/new/
    path('station/new/', views.fuel_station_new, name='fuel_station_new'),
    # ex: /station/5/
    path('station/<int:fuel_station_id>/', views.fuel_station_detail, name='fuel_station_detail'),

    # PURCHASE PATTERN
    # ex: /purchase/new/
    path('purchase/new/', views.receipt_new, name='receipt_new'),
    # ex: /purchase/3/
    path('purchase/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),

    # VEHICLE PATTERN
    # ex: /vehicle/new/
    path('vehicle/new/', views.vehicle_new, name='vehicle_new'),
    # ex: /vehicle/4/
    path('vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]
