
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showfood, name='showfood'),
    path('delete/<int:id>/', views.deleted_item, name='deleteitem'),
]
