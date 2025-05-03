from django.urls import path
from .views import what_am_i_doing

urlpatterns = [
    path('what-am-i-doing/', what_am_i_doing)
]