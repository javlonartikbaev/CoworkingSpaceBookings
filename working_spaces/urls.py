from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('types', TypeOfWorkingSpaceViewSet, basename='type_of_working_space')
router.register('spaces', WorkingSpacesViewSet, basename='working_space')

urlpatterns = [
    path('', include(router.urls))
]
