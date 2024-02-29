# booking/urls.py
from django.urls import path
from .views import BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    # path('list/', BookingView.as_view(), name='booking-list'),
    path('lists/', BookingListCreateView.as_view(), name='booking-lists'),
    path('details/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail'),

]
