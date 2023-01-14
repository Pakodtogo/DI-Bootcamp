from django.db import models

# Create your models here.
class Costumer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        ordering = ['firstname', 'lastname']


class VehicleSize(models.Model):
    sname = models.CharField(max_length=50)

    def __str__(self):
        return self.sname


class VehicleType(models.Model):
    tname = models.CharField(max_length=50)

    def __str__(self):
        return self.tname
    


class Vehicle(models.Model):
    vtype = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vsize = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    datecreated = models.DateField() 
    realcost = models.IntegerField()
    

    def __str__(self):
        return f'{self.vsize} {self.vtype} '


class Rental(models.Model):
    rentaldate = models.DateField()
    returndate = models.DateField(null=True, blank=True)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        ordering = ['rentaldate', 'returndate']
    
    def save(self, *args, **kwargs):
     if(self.returndate > self.rentaldate):
        super(Rental, self).save(*args, **kwargs)
     else:
        raise Exception ("Return date should be greater than rental date" )


    

class RentalRate(models.Model):
    dailyrate = models.FloatField()
    vehicletype = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehiclesize = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)