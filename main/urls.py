from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
	path('', views.main, name="home"),
	path('nucleus', views.Nucleus, name="Nucleus"),
	path('cell-membrane', views.cell_mem, name="cell_mem"),

]