# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BannerVideo
from .serializers import BannerVideoSerializer

@api_view(['GET'])
def home_video_view(request):
    latest_video = BannerVideo.objects.order_by('-uploaded_at').first()
    serializer = BannerVideoSerializer(latest_video, context={'request': request}) if latest_video else None
    return Response({
        "page": "Home",
        "content": "This is the Home page.",
        "video": serializer.data if serializer else None
    })


@api_view(['GET'])
def salons_view(request):
    return Response({"page": "Salons", "content": "This is the Salons page."})

@api_view(['GET'])
def cosmetics_view(request):
    return Response({"page": "Cosmetics", "content": "This is the Cosmetics page."})

@api_view(['GET'])
def event_hall_view(request):
    return Response({"page": "Event Hall", "content": "This is the Event Hall page."})

@api_view(['GET'])
def food_court_view(request):
    return Response({"page": "Food Court", "content": "This is the Food Court page."})

@api_view(['GET'])
def designing_view(request):
    return Response({"page": "Designing & Stitching", "content": "This is the Designing & Stitching page."})

@api_view(['GET'])
def academy_view(request):
    return Response({"page": "Academy", "content": "This is the Academy page."})

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


