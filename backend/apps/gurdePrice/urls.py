from django.urls import path
from .views import GuidePriceListCreateView, GuidePriceDetailView, guide_price_stats, guide_price_chart_data, export_guide_price

urlpatterns = [
    path('', GuidePriceListCreateView.as_view(), name='guide-price-list-create'),
    path('<int:pk>/', GuidePriceDetailView.as_view(), name='guide-price-detail'),
    path('stats/', guide_price_stats, name='guide-price-stats'),
    path('chart-data/', guide_price_chart_data, name='guide-price-chart'),
    path('export/', export_guide_price, name='guide-price-export'),
]