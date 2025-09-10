from django.urls import path
from .views import UserProfileView, user_detail_view

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/', user_detail_view, name='user-detail'),
]