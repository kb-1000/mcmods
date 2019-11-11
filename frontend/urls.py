from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('create/', views.CreateProjectView.as_view(), name='create_project'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
