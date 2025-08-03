from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Ride

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    User = get_user_model()

    class Meta:
        User = get_user_model()
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        return self.User.objects.create_user(**validated_data)
    

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ['rider', 'status', 'driver', 'created_at', 'updated_at']

class RideStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']

class RideLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['current_location']