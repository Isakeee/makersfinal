from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ImageView, OrderCreateView, \
                   FavouriteCreateView

router = DefaultRouter()
router.register('products', ProductViewSet, basename="Product")


urlpatterns = [
    path('', include(router.urls)),
    path('order/', OrderCreateView.as_view()),
    path('favourite/', FavouriteCreateView.as_view()),
    path('image', ImageView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]