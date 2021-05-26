from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import BankDetail
from .serializers import BankDetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .customlimitoffset import customlimitoffset
# Create your views here.

class index(ListAPIView):
	queryset = BankDetail.objects.all()
	serializer_class = BankDetailSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['^branch']
	pagination_class = customlimitoffset
	ordering_fields = ['ifsc']

class branches(ListAPIView):
	queryset = BankDetail.objects.all()
	serializer_class = BankDetailSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['^ifsc','^bank_id','^branch','^address', '^city', '^district', '^state']
	pagination_class = customlimitoffset
	ordering_fields = ['ifsc']
