from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import current_user, RegisterApi
from .views import UserList, UserDetail
from .views import LocationList, LocationDetail


urlpatterns = [
    # Authenication (JWT)
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),

    # AllowAny
    path("register/", RegisterApi.as_view()),

    # IsAuthenticated
    path("current_user/", current_user),
    path("users/", UserList.as_view()),
    path("users/<str:username>/", UserDetail.as_view()),
    path("locations/", LocationList.as_view()),
    path("locations/<str:name>/", LocationDetail.as_view()),
]
