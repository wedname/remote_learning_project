from rest_framework import serializers

from .models import Teachers, Students, Schedule, SubjectsTeachers


class StudentsListSerializer(serializers.ModelSerializer):
    """Список учеников"""

    user = serializers.SlugRelatedField(slug_field="fio", read_only=True)
    groups = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Students
        fields = ('user', 'group')


class TeachersListSerializer(serializers.ModelSerializer):
    """Список учителей"""

    credentials = serializers.SlugRelatedField(slug_field="fio", read_only=True)

    class Meta:
        model = Teachers
        fields = ('credentials',)


class SubjectsTeachersListSerializers(serializers.ModelSerializer):
    """Список учителей и их предметов"""

    teacher = TeachersListSerializer(read_only=True)
    subject = serializers.SlugRelatedField(slug_field="subject_name", read_only=True)

    class Meta:
        model = SubjectsTeachers
        fields = ('teacher', 'subject')


class ScheduleListSerializer(serializers.ModelSerializer):
    """Расписание"""
    group = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subject_teacher = SubjectsTeachersListSerializers(read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
