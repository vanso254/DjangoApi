from django.urls import path
from . import views

urlpatterns = [
    path("inventory/", views.InventoryListView.as_view(), name="inventory-list-create"),
    path("inventory/<int:pk>/delete/", views.InventoryDeleteView.as_view(), name="inventory-delete"),
    path("inventory/add/", views.InventoryCreateView.as_view(), name="inventory-create"),
    path("inventory/<int:pk>/", views.InventoryDetailView.as_view(), name="inventory-detail"),
    
]