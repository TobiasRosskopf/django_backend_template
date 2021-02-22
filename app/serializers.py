from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

# Import models
from .models import CustomUser
from .models import Location


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )
        return user


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


class LocationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Location
        fields = (
            "id",
            "name",
            "geom",
        )
        geo_field = "geom"
