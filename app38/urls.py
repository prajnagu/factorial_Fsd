from django.urls import path
from app38.views import home
urlpatterns = [path('', home,name='home'),]