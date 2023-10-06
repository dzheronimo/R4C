from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewRobot


app_name = 'api'

router = DefaultRouter()
router.register('newrobot', NewRobot, 'newrobot')
urlpatterns = [
    path('', include(router.urls))
]