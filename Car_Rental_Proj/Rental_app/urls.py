# # from django.urls import path,include
# from rest_framework.routers import DefaultRouter

# # from .views import RegisterView
# from django.urls import path
# from .views import RegisterView,LoginView, VehicleViewSet

# router = DefaultRouter()
# router.register(r'register', RegisterView, basename='register')
# router.register("vehicles", VehicleViewSet, basename="vehicle")




# # urlpatterns = [
# #     path('auth/register/', RegisterView.as_view(), name='register'),
    
# # ]


# # urlpatterns = [
# #     path('register/', RegisterView.as_view(), name='register'),
# #     path('login/', LoginView.as_view(), name='login'),
# #     path('vehicles/', VehicleViewSet.as_view({'get': 'list', 'post': 'create'}), name='vehicle-list'),
# # ]


from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AdminStatsView,
    BookingViewSet,
    FavoriteViewSet,
    FilterOptionsView,
    LoginView,
    OwnerBookingViewSet,
    PaymentWebhookView,
    RegisterView,
    ReviewViewSet,
    VehicleImageViewSet,
    VehicleViewSet,
)

router = DefaultRouter()
router.register("vehicles", VehicleViewSet, basename="vehicle")
router.register("vehicle-images", VehicleImageViewSet, basename="vehicle-image")
router.register("reviews", ReviewViewSet, basename="review")
router.register("favorites", FavoriteViewSet, basename="favorite")
router.register("bookings", BookingViewSet, basename="booking")
router.register("owner-bookings", OwnerBookingViewSet, basename="owner-booking")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("filters/", FilterOptionsView.as_view(), name="filters"),
    path("payments/webhook/", PaymentWebhookView.as_view(), name="payment-webhook"),
    path("admin/stats/", AdminStatsView.as_view(), name="admin-stats"),
    path("", include(router.urls)),
]
