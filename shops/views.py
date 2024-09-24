from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import *

# My views

class RegisterAccount(APIView):
    """
    Для регистрации покупателей
    """
    # реализуем метод отправки данных 

    def post(self, request):
        pass
