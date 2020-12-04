from rest_framework import serializers

from .models import UserRegistrar


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = UserRegistrar
        fields = (
            "registrar_fname",
            "registrar_lname",
            "registrar_username",
            "registrar_email",
            "registrar_phone",
            "password",
        )

    def create(self, validated_data):

        user = UserRegistrar.objects.create_user(
            registrar_fname=validated_data["registrar_fname"],
            registrar_lname=validated_data["registrar_lname"],
            registrar_username=validated_data["registrar_username"],
            registrar_email=validated_data["registrar_email"],
            registrar_phone=validated_data.get("registrar_phone", ""),
            password=validated_data.get("password"),
        )

        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrar
        fields = ("registrar_username", "password")
