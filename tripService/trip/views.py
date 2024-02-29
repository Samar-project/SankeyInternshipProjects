import json
import requests
from django.shortcuts import render
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Trip
from rest_framework import status,generics
from rest_framework.response import Response
# from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from .models import Trip
from .serializers import TripSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TripView(View):
    def post(self, request, *args, **kwargs):
        try:
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})





class TripRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def details(self, request, *args, **kwargs):
        pass



    
class TripListCreateView(generics.ListCreateAPIView):
    
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination
    ordering_fields = ['ticket_id', 'trip_id', 'traveller_name', 'ticket_cost', 'traveller_email']
    search_fields = ['ticket_id', 'traveller_name', 'traveller_email']
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # ...

def post(self, request, *args, **kwargs):
    try:
        # data = json.loads(request.body.decode('utf-8'))

        # # Store data in the Trip table
        # trip = Trip.objects.create(
        #     user_id=data['user_id'],
        #     vehicle_id=data['vehicle_id'],
        #     route_id=data['route_id'],
        #     driver_name=data['driver_name'],
        #     trip_distance=data['trip_distance']
        # )
        data=Trip.objects.all()
        data=data['user_id']
        print(data)
        # Transfer necessary data to the Booking table
        # Example: Make an API call to the Booking app
        response = requests.post('http://127.0.0.1:8001/booking/lists/',
                                 data=json.dumps({'trip_id': trip.trip_id}), headers={'Content-Type': 'application/json'})
        print(response)
        # Check if the response contains JSON
        try :
            booking_response = response.json()
            print(response.status_code)
            print(response.json())

        except json.JSONDecodeError:
            booking_response = {'status': 'error', 'message': 'Empty response from booking service'}

        return JsonResponse({'status': 'success', 'booking_response': booking_response})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
