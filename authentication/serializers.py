# serializers.py
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


