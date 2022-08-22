from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from .serializer import RegisterSerializer
# from . import models

class logout(APIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class register(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():            
            accounts = serializer.save()
            
            data['response'] = 'Account created successfully'
            data['username'] = accounts.username
            data['email'] = accounts.email
            # data['token'] = Token.objects.get(user=accounts).key
            refresh = RefreshToken.for_user(accounts)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            