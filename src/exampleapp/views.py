import logging

from exampleapp import models, serializers

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    """
    Return information about task.
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = (IsAuthenticated, )
    queryset = models.Task.objects.all()

    def create(self, request):
        """
        Submit a new task.
        """
        task_serializer = serializers.TaskSerializer(data=request.data)
        task_serializer.is_valid(raise_exception=True)

        logging.info("Creating task")
        # task submit
        task = models.Task()
        task.description = request.data.get("description")
        task.save()
        logging.info("Task created")

        return Response({"msg": "Task created"}, status=status.HTTP_201_CREATED)


    def list(self, request):
        """
        List all the tasks.
        """
        qs = models.Task.objects.all()
        task_serializer = serializers.TaskSerializer(qs, many=True)

        return Response(task_serializer.data, status=status.HTTP_200_OK)


# class TicketViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.TaskSerializer
#     permission_classes = (IsAuthenticated, )
#     queryset = models.Ticket.objects.all()
#
#     def create(self, request):
#         """
#         Submit a new task.
#         """
#         task_serializer = serializers.TaskSerializer(data=request.data)
#         task_serializer.is_valid(raise_exception=True)
#
#         logging.info("Creating task")
#         # task submit
#         task = models.Task()
#         task.description = request.data.get("description")
#         task.save()
#         logging.info("Task created")
#
#         return Response({"msg": "Task created"}, status=status.HTTP_201_CREATED)
#
#
#     def list(self, request):
#         """
#         List all the tasks.
#         """
#         qs = models.Task.objects.all()
#         task_serializer = serializers.TaskSerializer(qs, many=True)
#
#         return Response(task_serializer.data, status=status.HTTP_200_OK)


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Ticket.objects.filter(user=user).order_by('-travel_date')

    def create(self, request):
        task_serializer = serializers.TicketSerializer(data=request.data)
        task_serializer.is_valid(raise_exception=True)

        ticket = models.Ticket()
        ticket.name = request.data.get("name")
        print(type(request.user))

        ticket.user = User.objects.get(pk=request.user.pk)
        ticket.save()

        return Response({"msg": "Ticket added successfully"}, status=status.HTTP_201_CREATED)
