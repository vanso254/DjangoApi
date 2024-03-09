from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.views import APIView
from .models import Inventory
from .serializers import InventorySerializer


# Create your views here.
# A class to view all the inventory
class InventoryListView(APIView):
    def get(self, request):
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)
    
    
    #A Class to delete an inventory record
class InventoryDeleteView(DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

#creating a new Inventory record
class InventoryCreateView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class InventoryDetailView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer