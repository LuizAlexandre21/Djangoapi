from django.urls import path

from . import views

urlpatterns = [
  path(r'todos/', views.AlertasListView.as_view()),
  path(r'todos/<int:id>/', views.AlertasListView.as_view()),
]
