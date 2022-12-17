from django.urls import path
from WEB_LR.views import inicio

urlpatterns = [
    path('', inicio, name='home'),
]