from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,auth

User=get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    conf_password=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=["username","password","conf_password","email","first_name","last_name"]

    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password=self.validated_data["password"]
        conf_password=self.validated_data["conf_password"]
        email=self.validated_data['email']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'A user with the same email already exists'})
        elif password!=conf_password:
            raise serializers.ValidationError({'password':'Password does not match'})
            
        reg.set_password(password)
        reg.save()
        return reg