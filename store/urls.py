from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'store'
urlpatterns = [
    
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/', views.products, name="products"),
    path('accounts/', include('django.contrib.auth.urls')),
	path('signup/', views.signup, name='signup'),
	path('accounts/login/',auth_views.LoginView.as_view(template_name='registration/login.html')),
	path('accounts/logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html')),
	path('search_bar', views.search_bar, name="search_bar"),
    
]