from django import forms
from .models import Rental
from .models import Vehicle
from .models import Costumer


class CostumerForm(forms.ModelForm):
    class Meta:
        model= Costumer
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'address', 'city', 'country', ]
        #fields = '__all__'     this is another way of defining 'fields' variable
        
        labels = {
        
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'email',
            'phonenumber': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'country': 'Country'
        }

        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }

"""class RentalForm(forms.ModelForm):
    class Meta:
        model= Rental
        fields = ['rental_date', 'return_date', 'costumer', 'vehicle', ]
        #fields = '__all__'     this is another way of defining 'fields' variable
        labels = {
            'rentaldate': 'Rental Date',
            'returndate': 'Return Date',
            'costumer': 'Costumer',
            'vehicle': 'Vehicle'
    
        }

        widgets = {
            'rentaldate': forms.DateInput(attrs={'class': 'form-control'}),
            'returndate': forms.DateInput(attrs={'class': 'form-control'}),
            'costumer': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle': forms.TextInput(attrs={'class': 'form-control'})
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model= Vehicle
        fields = ['vtype', 'vsize', datecreated', 'realcost', ]
        #fields = '__all__'     this is another way of defining 'fields' variable
        labels = {
            'vtype': 'Vehicle Type',
            'vsize': 'Vehicle Size',
            'datecreated': 'Date Created',
            'realcost': 'Real Cost'
    
        }

        widgets = {
            'vtype': forms.TextInput(attrs={'class': 'form-control'}),
            'vsize': forms.TextInput(attrs={'class': 'form-control'}),
            'datecreated': forms.DateInput(attrs={'class': 'form-control'}),
            'realcost': forms.NumberInput(attrs={'class': 'form-control'})
        }"""


        