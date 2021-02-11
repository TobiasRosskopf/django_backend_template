from django.urls import path

from .views import current_user, signup
from .views import UserList, UserDetail
from .views import LocationList, LocationDetail


urlpatterns = [
    # AllowAny
    path("signup/", signup),

    # IsAuthenticated
    path("current_user/", current_user),
    path("users/", UserList.as_view()),
    path("users/<str:username>/", UserDetail.as_view()),
    path("locations/", LocationList.as_view()),
    path("locations/<str:name>/", LocationDetail.as_view()),
]
