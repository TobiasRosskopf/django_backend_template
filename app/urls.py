from django.urls import path

from .views import current_user, UserList, UserDetail, signup


urlpatterns = [
    # AllowAny
    path("signup/", signup),

    # IsAuthenticated
    path("current_user/", current_user),
    path("users/", UserList.as_view()),
    path("users/<str:username>/", UserDetail.as_view()),
]
