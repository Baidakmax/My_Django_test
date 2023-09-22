"""
URL configuration for my_first_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from rest_framework import routers
from catalog.views import TagViewSet, GoodViewSet, CategoryViewSet, HelloView, CategoryListView, \
    CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

admin.site.site_header = "Baidak Admin"
admin.site.site_title = "Baidak Admin Portal"
admin.site.index_title = "Welcome to Baidak Admin Portal"



Router = routers.DefaultRouter()
Router.register('tag', TagViewSet)
Router.register('good', GoodViewSet)
Router.register('category', CategoryViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Catalog API",
        default_version='v1',
        description="Catalog API",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swaggerBlog.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)






urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(Router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path("category_detail/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path('hello/', HelloView.as_view(), name='hello'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # path("category_list/", CategoryViewSet.as_view({'get': 'list'}), name='category_list'),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




