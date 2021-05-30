
from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url
from BankApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/branches/autocomplete',views.index.as_view(), name="Banks"),
	path('api/branches',views.branches.as_view(), name="Branches"),
]
