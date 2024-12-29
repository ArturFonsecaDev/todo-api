from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserView, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]