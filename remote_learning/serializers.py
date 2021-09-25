from rest_framework import serializers

from .models import Students


class StudentsListSerializer(serializers.ModelSerializer):
    """Список учеников"""

    # user = serializers.SlugRelatedField(slug_field="")

    class Meta:
        model = Students
        fields = ('user', 'group')
