from django.http import Http404

from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Import models
from .models import CustomUser
from .models import Location

# Import serializers
from .serializers import RegisterSerializer
from .serializers import UserSerializer
from .serializers import LocationSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully.",
        })


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, username, format=None):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, name):
        try:
            return Location.objects.get(name=name)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        location = self.get_object(name)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def delete(self, request, name, format=None):
        location = self.get_object(name)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
