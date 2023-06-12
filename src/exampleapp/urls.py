from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from exampleapp import views

router = DefaultRouter()
router.register("tasks", views.TaskViewSet, "task")
router.register(r'tickets', views.TicketViewSet, "ticket")

urlpatterns = [
    re_path("", include(router.urls))
]