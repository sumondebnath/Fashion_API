from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from account.models import UserAccount, UserAddress
from account.constants import ACCOUNT_TYPE
from django.contrib.auth.models import User

class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class UserAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE)
    class Meta:
        model = User 
        fields = ["username", "first_name", "last_name", "email", "account_type", "password", "confirm_password"]

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        account_type = self.validated_data["account_type"]
        print(account_type)
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            return serializers.ValidationError({"error":"Password Does Not Matched!"})
        if User.objects.filter(email=email).exists():
            return serializers.ValidationError({"error":"Email Already Exists!"})
        
        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        
        account.set_password(password)
        if account_type == "Admin":
            account.is_staff = True
            account.is_superuser = True
        # else:
        #     account.is_staff = False
        #     account.is_superuser = False
        account.save()

        user_acc = UserAccount(user = account, account_type=account_type)
        user_acc.save()
        return account





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)





class ChangePasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        old_password = attrs.get("old_password")
        password = attrs.get("password")
        password2 = attrs.get("password2")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError("User not found")

        if not user.check_password(old_password):
            raise ValidationError("Old password is not correct")

        if password != password2:
            raise ValidationError("New password fields didn't match")

        return attrs

    def save(self):
        user_id = self.validated_data["user_id"]
        password = self.validated_data["password"]

        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()