from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.app,name="app"),
    path('index',views.index,name="index"),
    path('dash',views.dash,name="dash")
]