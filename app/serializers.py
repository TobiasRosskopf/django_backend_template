from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_jwt.settings import api_settings

# Import models
from .models import CustomUser
from .models import Location


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "last_login",
        )


class UserSerializerWithToken(ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

    class Meta:
        model = CustomUser
        fields = ("token", "username", "password")


class LocationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Location
        geo_field = "geom"
        fields = ("id", "name", "geom")
