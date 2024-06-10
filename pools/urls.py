from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="pools_index")
]
