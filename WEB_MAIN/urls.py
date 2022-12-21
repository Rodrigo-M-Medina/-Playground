from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WEB_LR.urls')),
    path('blog/', include('WEB_BLOG.urls')),
]
