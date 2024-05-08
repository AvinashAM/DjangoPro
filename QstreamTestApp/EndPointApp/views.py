from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data.get('data').get('attributes'))
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUsers(APIView):
    def get(self, request):
        sort_field = request.query_params.get('sort', 'first_name')
        if sort_field not in ['first_name', 'last_name', 'email_address', 'country']:
            sort_field = 'first_name'  # Default sorting field

        users = User.objects.all().order_by(sort_field)
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)