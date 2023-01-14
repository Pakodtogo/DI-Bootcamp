from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
   path('rent/rental',views.rental, name='rental'),
   path('rent/rental/<int:id>', views.rental_details, name='rental_details'),
   path('rent/rental_add', views.rental_add, name='rental_add'),
   path('rent/costumer/<int:id>', views.costumer_details, name='costumer_details'),
   path('rent/costumer/', views.costumer, name='costumer'),
   path('rent/costumer_add', views.costumer_add, name='costumer_add'),
   path('rent/costumer/<int:id>', views.costumer_delete, name='costumer_delete'),
   path('rent/vehicle/<int:id>', views.vehicle_details, name='vehicle_details'),
   path('rent/vehicle/', views.vehicle, name='vehicle'),
   path('rent/vehicle_add', views.vehicle_add, name='vehicle_add'),
]
