from app.serializers import UserSerializer


def jwt_response_handler(token, user=None, request=None):
    return {
        "token": token,
        "username": user.username,
    }
