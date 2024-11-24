from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, BannerListCreateView, CartListView, OrderListView,ProductDetailView
from .views import RegisterView, LoginView, LogoutView,ProfileView, CartDetailView,OrderDetailView,OrderCreateView,OrderItemDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'), 
    path('orders/create/', OrderCreateView.as_view(), name='order-create'), 
    path('orders/<int:order_id>/delete/', OrderItemDeleteView.as_view(), name='order-delete'),
    path('orders/<int:order_id>/items/<int:order_item_id>/delete/', OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]