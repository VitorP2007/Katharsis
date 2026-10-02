app_name = 'conteudos'

from django.urls import path

from . import views

urlpatterns = [
	path('', views.lista, name='lista'),
	path('<int:pk>/', views.detalhe, name='detalhe'),
]
