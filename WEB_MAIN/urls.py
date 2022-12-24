from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WEB_LR.urls')),
    path('blog/', include('WEB_BLOG.urls')),
]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)