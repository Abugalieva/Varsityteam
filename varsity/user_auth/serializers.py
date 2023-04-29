from rest_framework import serializers
from user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = "__all__"


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, max_length=20)
    new_password = serializers.CharField(min_length=8, max_length=20)
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False, allow_blank=False)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8, max_length=20)