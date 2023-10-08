from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url='admin/'), name="admin"),
   # path('dashboard/', include('home.dashboard_urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('home.urls')),
    path('api/',include('products.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)