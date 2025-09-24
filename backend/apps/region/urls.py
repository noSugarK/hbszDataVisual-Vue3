from django.urls import path
from .views import RegionListCreateView, RegionDetailView, region_tree

urlpatterns = [
    path('', RegionListCreateView.as_view(), name='region-list-create'),
    path('tree/', region_tree, name='region-tree'),
    path('<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
]
