from django.urls import path
from .views import UserProfileView, UserDetailView, UserListView, check_username_exists, check_email_exists

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('check-username/', check_username_exists, name='check-username'),
    path('check-email/', check_email_exists, name='check-email'),
]