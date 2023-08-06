from django.shortcuts import render
from django_filters import rest_framework as filters
from  rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import TagSerializer, GoodSerializer, CategorySerializer
from  rest_framework import filters as drf_filters
from .models import Tag, Good, Category
from .filters import GoodsFilter

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Good.objects.filter(active=True)
    serializer_class = GoodSerializer
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter)
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    filterset_class = GoodsFilter


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().prefetch_related('goods')
    serializer_class = CategorySerializer