from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CategoryViewSet, FoodTypeViewSet, IngredientViewSet, OrderViewSet,
    register_user, login_user, user_profile, health_check
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'food-types', FoodTypeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/profile/', user_profile, name='profile'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('health/', health_check, name='health_check'),
]
