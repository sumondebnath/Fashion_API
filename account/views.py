from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from account.models import UserAccount, UserAddress
from account.serializers import UserAccountSerializers, UserAddressSerializers, RegistrationSerializer, LoginSerializer, ChangePasswordSerializer
from rest_framework.exceptions import ValidationError

from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import login, authenticate, logout

# Create your views here.

class UserAccountViewsets(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.query_params.get("user_id")
        print(user_id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class UserAddressViesets(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.query_params.get("user_id")

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    


class RegistrationViewset(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(token, uid)
            return Response({"message": "Registration successful!"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError(serializer.errors)
    


class LoginViewset(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                print(token, created)
                login(request, user)
                return Response({"token":token.key, "user_id":user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ChangePasswordViewset(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutViewset(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
         # return redirect('login')
        return Response({'success' : "logout successful"}, status=status.HTTP_200_OK)