from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin

from .models import (
    Groups,
    Students,
    Subjects,
    Teachers,
    SubjectsTeachers,
    Schedule,
    Tasks,
    Grades,
    StudentsAnswers,
    User
)


@admin.register(User)
class CustomUserAdmin(OrigUserAdmin):
    exclude = ('first_name', 'last_name')
    fieldsets = (
        ('Персональная информация', {'fields': ('fio', 'email', 'password')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
        ('Разрешения', {'fields': ('is_active', 'is_teacher', 'is_student')}),
    )


admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(SubjectsTeachers)
admin.site.register(Schedule)
admin.site.register(Tasks)
admin.site.register(Grades)
admin.site.register(StudentsAnswers)
