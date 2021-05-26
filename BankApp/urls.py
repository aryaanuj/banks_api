from django.urls import path, include
from BankApp import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('Bank-Detail', views.index, basename="Banks")
urlpatterns = [
	path('branches/autocomplete',views.index.as_view(), name="Banks"),
	path('branches',views.branches.as_view(), name="Branches"),
]