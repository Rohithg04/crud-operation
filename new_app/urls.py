from django.urls import path

from new_app import views

urlpatterns = [
    path('view',views.app,name="app"),
    path('',views.index,name="index"),
    path('dash',views.dash,name="dash"),
    path('submit',views.submit,name="submit"),
    path('WaterLand_view',views.WaterLand_view,name="WaterLand_view"),
    path('delete/<int:id>/',views.WaterLand_delete,name="WaterLand_delete"),
    path('update/<int:id>/', views.WaterLand_update, name="WaterLand_update")

]