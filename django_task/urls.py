from django.urls import include, path
from rest_framework import routers
from myapp import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet , basename='User')
router.register(r'activityperiod', views.ActivityPeriodViewSet, basename='ActivityPeriod')

urlpatterns = [
    path('', include(router.urls)),
]