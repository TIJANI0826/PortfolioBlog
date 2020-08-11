from . import views
from django.urls import path
urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]
