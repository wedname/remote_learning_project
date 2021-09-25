from django.contrib import admin
from .models import Groups, Students, Subjects, Teachers, SubjectsTeachers, Schedule, Tasks, Grades, StudentsAnswers, User


admin.site.register(User)
admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(SubjectsTeachers)
admin.site.register(Schedule)
admin.site.register(Tasks)
admin.site.register(Grades)
admin.site.register(StudentsAnswers)
