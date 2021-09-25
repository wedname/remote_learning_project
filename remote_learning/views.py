from rest_framework import generics

from .permissions import StudentOnly
from .models import Schedule, Students
from .serializers import (
    ScheduleListSerializer
)


class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleListSerializer
    permission_classes = [StudentOnly]

    def get_queryset(self):
        student = Students.objects.get(credentials=self.request.user)
        schedule = Schedule.objects.filter(group=student.group)
        return schedule
