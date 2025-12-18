from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.admin import ecommerce_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/admin/', ecommerce_admin_site.urls),
    path('', include('app.urls')),
]

# In production, you should serve MEDIA via Nginx/Apache or object storage.
# This fallback keeps uploaded images working even when DEBUG=False.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
