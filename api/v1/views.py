from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core import models
from core.services import create_payment_intent
from django.shortcuts import get_object_or_404


class Order(APIView):
    def post(self, request, pk):
        order = get_object_or_404(models.Order, pk=pk)

        try:
            client_secret = create_payment_intent(order)
            return Response({'client_secret': client_secret}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)