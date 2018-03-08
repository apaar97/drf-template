from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='API', public=False)),
]
