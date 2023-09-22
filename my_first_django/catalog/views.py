from django.shortcuts import render
from time import timezone
from django.urls import reverse_lazy
from django_filters import rest_framework as filters
from  rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import TagSerializer, GoodSerializer, CategorySerializer
from  rest_framework import filters as drf_filters
from .models import Tag, Good, Category
from .filters import GoodsFilter
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().prefetch_related('goods')
    serializer_class = CategorySerializer

class HelloView(TemplateView):
    template_name = 'about.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'category-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = "timezone.now()"
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = 'timezone.now()'
        return context


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category_create.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    # template_name_suffix = "_update_form"
    template_name = 'category_update.html'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")
    template_name = 'category_delete.html'