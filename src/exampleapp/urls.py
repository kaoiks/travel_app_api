from django.conf.urls import include
from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from exampleapp import views

router = DefaultRouter()
router.register("tasks", views.TaskViewSet, "task")
router.register(r'tickets', views.TicketViewSet, "ticket")

urlpatterns = [
    re_path("", include(router.urls)),
    # path('ticket/<int:ticket_id>/set-file/', views.set_ticket_file, name="set_ticket_file")
]