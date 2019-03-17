from django.urls import path
from .views import product_detail_view, product_create_view, dynamic_lookup_view

app_name = 'myapp'
urlpatterns = [
    path('', product_detail_view, name='detail-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view, name="create"),
]