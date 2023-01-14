from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from rent.models import Rental
from rent.models import Costumer
from rent.models import Vehicle
from rent.models import VehicleSize
from rent.models import VehicleType
from rent.models import RentalRate
from rent.forms import CostumerForm


# Create your views here.

def index(request):
    return render(request, "rent/index.html")


def vehicle(request):
    return render(request, "rent/vehicle.html", {
        'vehicles': Vehicle.objects.all()
    })

def costumer(request):
    return render(request, "rent/costumer.html", {
        'costumers': Costumer.objects.all()
    })

def rental(request):
    return render(request, "rent/rental.html", {
        'rentals': Rental.objects.all()
    })

def rental_details(request, id):
    rental= Rental.objects.get(pk=id)
    return HttpResponseRedirect(reverse('rental'))

def vehicle_details(request, id):
    vehicle= Vehicle.objects.get(pk=id)
    return HttpResponseRedirect(reverse('vehicle'))

def costumer_details(request, id):
    costumer= Costumer.objects.get(pk=id)
    return HttpResponseRedirect(reverse('costumer'))



def rental_add(request):
    costum = Costumer.objects.all()
    vehicl = Vehicle.objects.all()
    if request.method == 'POST':
            new_costumer = request.POST.get('costumer')
            new_vehicle = request.POST.get('vehicle')
            new_rental_date = request.POST.get('rentaldate')
            new_return_date = request.POST.get('returndate')
           
            
            
            new_rental = Rental(
                
                costumer_id = new_costumer,
                vehicle_id = new_vehicle,
                rentaldate = new_rental_date,
                returndate = new_return_date
            )
            new_rental.save()
            return render(request, 'rent/rental_add.html',{
                'success':True
            })
    return render(request, 'rent/rental_add.html', {'costum':costum, 'vehicl':vehicl})

def vehicle_add(request):
    types = VehicleType.objects.all()
    sizes = VehicleSize.objects.all()
    if request.method == 'POST':
            new_vehicle_type = request.POST.get('vtype')
            new_size = request.POST.get('vsize')
            new_date_created = request.POST.get('datecreated')
            new_real_cost = request.POST.get('realcost')
            
            
            new_vehicle = Vehicle(
                vtype_id = new_vehicle_type,
                vsize_id = new_size,
                datecreated = new_date_created,
                realcost = new_real_cost
                
            )
            new_vehicle.save()
            return render(request, 'rent/vehicle_add.html',{
                'success':True
            })
    return render(request,'rent/vehicle_add.html', {'type':types, 'sise':sizes})



def costumer_add(request):
    if request.method == 'POST':
            new_first_name = request.POST.get('firstname')
            new_last_name = request.POST.get('lastname')
            new_email = request.POST.get('email')
            new_phone_number = request.POST.get('phonenumber')
            new_address = request.POST.get('address')
            new_city = request.POST.get('city')
            new_country = request.POST.get('country')
            
            
            new_costumer = Costumer(
                firstname = new_first_name,
                lastname = new_last_name,
                email = new_email,
                phonenumber = new_phone_number,
                address = new_address,
                city = new_city,
                country = new_country
            )
            new_costumer.save()
            return render(request, 'rent/costumer_add.html',{
                'success':True
            })
    return render(request, 'rent/costumer_add.html' )


def costumer_delete(request, id):
    if request.method == 'POST':
        costumer = Costumer.objects.get(pk=id)
        costumer.delete()
    return HttpResponseRedirect(reverse('costumer'))