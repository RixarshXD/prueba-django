from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderIndex, name='index'),
    path('elementos<str:categoria>/', views.renderContexto, name='productos')
]
