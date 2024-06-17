from django.urls import path

from . import views

app_name = "pools"
urlpatterns = [
  path("", views.IndexView.as_view(), name="questions"),
  path("<int:pk>/", views.DetailView.as_view(), name="question_detail"),
  path("<int:pk>/result", views.ResultView.as_view(), name="question_result"),
  path("<int:question_id>/vote", views.vote, name="question_vote")
]
