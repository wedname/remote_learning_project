from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", views.ScheduleListView.as_view()),
]
