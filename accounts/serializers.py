from rest_framework import serializers
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'last_login': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email, password=password, **validated_data)
            return user
        raise serializers.ValidationError('An user with this email already exists')
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.update_user(user_id=instance.pk, password=password, **validated_data)
        return user
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        
        if not password or not confirm_password:
            raise serializers.ValidationError('Password and Confirm Password fields are required!')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords must match.')
        
        return data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('confirm_password', None)
        return representation
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data['user'] = {
            'id': user.id,
            'email': user.email,
        }
        return data
