from django.urls import path
from WEB_BLOG.views import blog

urlpatterns = [
    path('blog/', blog),
]