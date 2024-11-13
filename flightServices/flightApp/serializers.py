from rest_framework import serializers
from .models import Passenger, Reservation, Flight
import re

def isFlightNumberValid(flightNumber):
    print("isFlightNumberValid")
    

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        validators = [isFlightNumberValid]
        
    def validate_flightNumber(self, flightNumber):
        print("validate_flightNumber")
        if (re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("항공편 번호가 올바르지 않음")
        return flightNumber
    
    def validate(self, data):
        print("validate")
        print(data['flightNumber'])
        return data
        
        
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"