import logging

from exampleapp import models, serializers

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action

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
        ticket.travel_date = request.data.get("travel_date", None)
        start_location = models.Location()
        start_location.name = request.data.get("start_location").get("name")
        start_location.latitude = request.data.get("start_location").get("latitude")
        start_location.longitude = request.data.get("start_location").get("longitude")

        start_location.save()

        end_location = models.Location()
        end_location.name = request.data.get("end_location").get("name")
        end_location.latitude = request.data.get("end_location").get("latitude")
        end_location.longitude = request.data.get("end_location").get("longitude")

        end_location.save()

        ticket.start_location = start_location
        ticket.end_location = end_location

        ticket.user = User.objects.get(pk=request.user.pk)
        ticket.save()
        ticket_serializer = serializers.TicketSerializer(ticket)
        return Response(ticket_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], name='Add file to ticket')
    def set_file(self, request, pk=None):
            try:
                ticket = models.Ticket.objects.get(id=pk)
                if ticket.user != request.user:
                    print(request.user)
                    print("WRONG USER")
                    return JsonResponse({'error': 'Unauthorized access'}, status=401)

            except models.Ticket.DoesNotExist:
                return JsonResponse({'error': 'Ticket not found'}, status=404)

            if request.method == 'POST':
                # Exclude travel_date from update
                request_data = request.data.copy()
                request_data.pop('travel_date', None)

                # Update file_field if provided in the request files
                if 'file' in request.FILES:
                    file = request.FILES['file']
                    ticket.file_field = file

                ticket.__dict__.update(request_data)
                ticket.save()
                return Response({'success': 'Ticket updated successfully'})

            return JsonResponse({'error': 'Invalid request'}, status=400)

