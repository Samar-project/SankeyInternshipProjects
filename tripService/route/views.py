from rest_framework.pagination import PageNumberPagination
from rest_framework import status,generics
from rest_framework.response import Response
from .models import Route
from .serializers import RouteSerializer

# Create your views here.

class RouteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    pagination_class = PageNumberPagination
    ordering_fields = ['ticket_id', 'Route_id', 'traveller_name', 'ticket_cost', 'traveller_email']
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