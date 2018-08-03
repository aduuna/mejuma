from django.urls import path

from mejuma.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    # path("login/", view=user_login, name="login"),
    # path("signup/", view=user_signup, name="signup"),
    # path("logout/", view=user_logout, name="logout"),
]
