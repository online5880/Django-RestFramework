from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)      # 항공기 번호
    operatingAirlines = models.CharField(max_length=20) # 항공사
    departureCity = models.CharField(max_length=20, blank=True, null=True)     # 출발 도시
    arrivalCity = models.CharField(max_length=20)       # 도착 도시
    dateOfDeparture = models.DateField()                # 출발 날짜
    estimatedTimeOfDeparture = models.TimeField()       # 출발 예정 시간
    
class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    
    
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        