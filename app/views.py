from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserSerializerWithToken

from .models import CustomUser


@api_view(["GET"])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

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
