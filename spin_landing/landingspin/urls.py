from django.urls import path
from landingspin import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]

handler404 = 'landingspin.views.handler404'