from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('salons/', views.salons_view),
    path('salons/<int:id>/', views.salons_detail_view),
    path('cosmetics/', views.cosmetics_view),
    path('event-hall/', views.event_hall_view),
    path('food-court/', views.food_court_view),
    path('designing-stitching/', views.designing_view),
    path('academy/', views.academy_view),
    path('franchise/', views.franchise_view),
    path('about-us/', views.about_us_view),
    path('contact/', views.contact_view),


    # ecom-----------------

    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("products/", views.ProductListAPIView.as_view(), name="product-list"),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),

    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),



  
]
