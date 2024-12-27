from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, ColumnViewSet, TaskViewSet

router = DefaultRouter()
router.register('todo', ToDoViewSet)
router.register('column', ColumnViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]