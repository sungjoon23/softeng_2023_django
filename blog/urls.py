from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('',views.index),
]

urlpatterns += staticfiles_urlpatterns()