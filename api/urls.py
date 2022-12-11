from django.urls import path
from .views import Index, add_subscriber, get_subscriber, get_enrollments, create_enrollment, get_random_transaction_id, login

urlpatterns = [
    path('', Index),
    path('add_subscriber/', add_subscriber),
    path('get_subscriber/<userID>/', get_subscriber),
    path('get_enrollments/<userID>/', get_enrollments),
    path('create_enrollment/', create_enrollment),
    path('get_random_transaction_id/', get_random_transaction_id),
    path('login/', login),
]
