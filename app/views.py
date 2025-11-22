# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BannerImage,Saloon,Cosmetics,FoodMenu,Courses,Cart,CartItem,Category
from .serializers import BannerImageSerializer,SaloonSerializer,CosmeticsSerializer,FoodMenuSerializer,CourseSerializer,CartItemSerializer,CartSerializer



@api_view(['GET'])
def home(request):
    latest_image = BannerImage.objects.order_by('-uploaded_at').first()
    serializer = BannerImageSerializer(latest_image, context={'request': request}) if latest_image else None
    return Response({
        "page": "Home",
        "content": "This is the Home page.",
        "video": serializer.data if serializer else None
    })


@api_view(['GET'])
def salons_view(request):
    salon = Saloon.objects.all()
    serializer = SaloonSerializer(salon, many=True, context={'request': request})
    return Response({
        "page": "Salons page",
        "data": serializer.data
    })

def Food_menu_view(request):
    food_items = FoodMenu.objects.all()
    serializer = FoodMenuSerializer(food_items, many=True, context={'request': request})
    return Response({
        "page": "Food Menu",
        "data": serializer.data
    })



@api_view(['GET'])
def salons_detail_view(request, id):
    try:
        salon = Saloon.objects.get(id=id)
        serializer = SaloonSerializer(salon, context={'request': request})
        return Response({
            "page": "Salon Detail",
            "data": serializer.data
        })
    except Saloon.DoesNotExist:
        return Response({"error": "Salon not found"}, status=404)

@api_view(['GET'])
def cosmetics_view(request):
    return Response({"page": "Cosmetics", "content": "This is the Cosmetics page."})

@api_view(['GET'])
def event_hall_view(request):
    return Response({"page": "Event Hall", "content": "This is the Event Hall page."})

@api_view(['GET'])
def food_court_view(request):
    food_items = FoodMenu.objects.all()
    serializer = FoodMenuSerializer(food_items, many=True, context={'request': request})
    return Response({
        "page": "Food Menu",
        "data": serializer.data
    })




@api_view(['GET'])
def designing_view(request):
    return Response({"page": "Designing & Stitching", "content": "This is the Designing & Stitching page."})



@api_view(['GET'])
def academy_view(request):
    courses = Courses.objects.all()
    course_serializer = CourseSerializer(courses, many=True, context={"request": request})
    return Response({
        "page": "course",
        "data": course_serializer.data
    })



@api_view(['GET'])
def franchise_view(request):
    return Response({"page": "Franchise", "content": "This is the Franchise page."})

@api_view(['GET'])
def about_us_view(request):
    return Response({"page": "About Us", "content": "This is the About Us page."})

@api_view(['GET'])
def contact_view(request):
    return Response({"page": "Contact", "content": "This is the Contact page."})


@api_view(['GET'])
def Buy_productes_view(request):
    return Response({"page": "Buy Products", "content": "This is the Buy Products page."})







# --------------------------ecommerse----------------------------

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    SignupSerializer, LoginSerializer,ProductVariantSerializer, ProductListSerializer, CategorySerializer,ProductDetailSerializer
)
from .models import Category, Product, ProductVariant

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate



# ----------------------------
# auth
# ----------------------------

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({
                "message": "Signup successful",
                "token": token.key
            }, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message":"Login successful",
                "token": token.key
            })
        return Response(serializer.errors, status=400)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()   # Delete token
        return Response({"message": "Logged out"}, status=200)


# -----------------------------------



class ProductListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProductDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductDetailSerializer(product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        



class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        variant_id = request.data.get("variant_id")
        quantity = int(request.data.get("quantity", 1))

        try:
            variant = ProductVariant.objects.get(id=variant_id)
        except ProductVariant.DoesNotExist:
            return Response({"error": "Variant not found"}, status=404)

        # Check stock
        if variant.stock < quantity:
            return Response({"error": "Not enough stock"}, status=400)

        # Get or create cart
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Get or create cart item
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant,
            defaults={'quantity': quantity}
        )

        if not item_created:
            if variant.stock < cart_item.quantity + quantity:
                return Response({"error": "Stock limit reached"}, status=400)

            cart_item.quantity += quantity
            cart_item.save()

        return Response({"message": "Added to cart successfully"}, status=200)
    

class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

        
        