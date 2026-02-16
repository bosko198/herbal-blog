from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('like/<int:post_id>/', views.like_post, name='like-post'),
    path('accounts/', include('django.contrib.auth.urls')), # For login/logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
