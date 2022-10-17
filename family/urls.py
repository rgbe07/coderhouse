from django.urls import path

from family import views

app_name = "family"
urlpatterns = [
    path("family", views.familys, name="family-list"),
]
