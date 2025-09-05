from django.urls import path
from .views import principal

urlpatterns=[
    path('', principal.as_view(), name='principal')
]