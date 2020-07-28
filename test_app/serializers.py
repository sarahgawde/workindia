from rest_framework import serializers 
from test_app.models import UserDetails
from django.contrib.auth.models import User

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('first_name','last_name')

class UserSerializer(serializers.ModelSerializer):
    user_acc=UserAuthSerializer()
    class Meta:
        model = UserDetails
        fields = '__all__'