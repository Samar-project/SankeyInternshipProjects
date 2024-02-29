from django.shortcuts import render
from django.views import View
from requests import request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .serializers import BookingSerializer
from .models import Booking



class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = PageNumberPagination
    ordering_fields = ['ticket_id', 'trip_id', 'traveller_name', 'ticket_cost', 'traveller_email']
    search_fields = ['ticket_id', 'traveller_name', 'traveller_email']
    

    

    def post(self, request, *args, **kwargs):
        try:
            # Access self.request here
            trip_id = request.data.get('trip_id')
            # Your booking creation logic here
            # ...

            # Create a Response object with custom data
            response_data = {
                'status': 'success',
                'trip_id': trip_id,
                # Other data you want to include in the response
            }
            return Response(response_data)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})
        
                
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if serializer: 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    