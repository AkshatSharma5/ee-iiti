from django.urls import path
from banana import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('read', views.GetBananaView.as_view()),
]
