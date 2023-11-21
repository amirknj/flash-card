from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateFlashCardSerializer, UpdateFlashCardSerializer
from django.shortcuts import get_object_or_404
from .models import FlashCard
from rest_framework import status


class CreateFlashCardView(APIView):
    def post(self, request):
        serializer = CreateFlashCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):
    def put(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        serializer = UpdateFlashCardSerializer(data=request.data, instance=flash_card)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
