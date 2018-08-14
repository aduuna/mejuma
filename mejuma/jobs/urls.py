from django.urls import path

from .views import (
    index,
)

app_name = "jobs"
urlpatterns = [
    path("", view=index, name="index"),
]
