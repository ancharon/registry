from django.conf.urls import patterns, url, include
from people import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'people', views.PersonViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)