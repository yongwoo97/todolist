from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer, LoginSerializer, EmailUniqueSerializer
from .models import User

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

# Create your views here.
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse(
            {
                "token": token.key
            }
        )

class EmailUniqueView(generics.GenericAPIView):

    serializer_class = EmailUniqueSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return JsonResponse({'detail': 'You can use this email'}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = serializer.errors['username'][0]
            return JsonResponse(detail, status=status.HTTP_400_BAD_REQUEST)
