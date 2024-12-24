from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
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
        email = validated_data.get('email', None)
        user = User.objects.create_user(email=email, password=password, **validated_data)
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.update_user(user_id=instance.pk, password=password, **validated_data)
        return user
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if not password or not confirm_password:
            raise serializers.ValidationError('Password and Confirm Password fields are required!')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords must match.')
        
        data.pop('confirm_password')
        return data