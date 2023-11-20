from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateUserSerializer
from django.contrib.auth.models import User


class UserCreate(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_data = User(
                username=data["username"],
                email=data["email"]
            )
            user_data.set_password(data["password"])
            user_data.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
