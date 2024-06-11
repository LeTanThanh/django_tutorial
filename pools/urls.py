from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="questions"),
  path("<int:question_id>/", views.detail, name="question_detail"),
  path("<int:question_id>/results/", views.results, name="question_results"),
  path("<int:question_id>/votes", views.vote, name="question_vote")
]
