from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetail, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products_detail'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update')
]
