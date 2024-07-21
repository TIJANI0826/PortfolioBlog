from django.urls import path
from . import views
app_name="projects"
urlpatterns = [
    path("projects",views.project_index,name="project_index"),
    path("projects/<int:pk>/",views.project_detail, name="project_detail"),
    path('', views.register, name='register'),
    path('payment-confirmation/', views.payment_confirmation, name='payment_confirmation'),
]

