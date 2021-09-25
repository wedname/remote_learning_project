from django.db import models
from datetime import date, datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователи"""
    first_name = None
    last_name = None
    fio = models.CharField(verbose_name='ФИО', max_length=255)
    REQUIRED_FIELDS = ['fio']


class Groups(models.Model):
    """Классы"""
    name = models.CharField(max_length=128, verbose_name='Класс')

    def __str__(self):
        return f"Класс: {self.name}"

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Students(models.Model):
    """Ученики"""
    credentials = models.OneToOneField(User, verbose_name='Ученик', related_name='student', on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, verbose_name='Класс', on_delete=models.CASCADE)

    def __str__(self):
        return f"Ученик: {self.credentials.fio}, класс: {self.group.name}"

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
        ordering = ['credentials__fio', 'group']


class Subjects(models.Model):
    """Предметы"""
    subject_name = models.CharField(max_length=255, verbose_name='Класс')

    def __str__(self):
        return f"{self.subject_name}"

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Teachers(models.Model):
    """Преподаватели"""
    credentials = models.OneToOneField(User, verbose_name='Ученик', related_name='teacher', on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subjects, blank=True, verbose_name='Записи на туры',
                                     related_name='teacher_subject', through="SubjectsTeachers")

    def __str__(self):
        return f"Преподаватель: {self.credentials.fio}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class SubjectsTeachers(models.Model):
    """Учителя и их предметы"""
    subject = models.ForeignKey(Subjects, verbose_name='Предмет', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, verbose_name='Преподаватель', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.subject_name} - {self.teacher.credentials.fio}"

    class Meta:
        verbose_name = "Учителя и их предметы"
        verbose_name_plural = "Учителя и их предметы"


class Schedule(models.Model):
    """Расписание"""
    subject_teacher = models.ForeignKey(SubjectsTeachers, verbose_name='Предмет и преподаватель',
                                        on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, verbose_name='Класс', on_delete=models.CASCADE)
    date = models.DateField("День", default=date.today)
    start_at = models.DateTimeField(default=datetime.now(), verbose_name="Начало")
    end_till = models.DateTimeField(default=datetime.now(), verbose_name="Конец")

    def __str__(self):
        return f'{self.group.name} | {self.date} | {self.subject_teacher.subject}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
        ordering = ['group', 'date']


class Tasks(models.Model):
    """Задания"""
    group = models.ForeignKey(Groups, verbose_name='Класс', on_delete=models.CASCADE)
    subject_teacher = models.ForeignKey(SubjectsTeachers, verbose_name='Предмет и преподаватель',
                                        on_delete=models.CASCADE)
    type_task = models.CharField(max_length=128, verbose_name='Тип задания')
    task = models.TextField(verbose_name='Задание')
    date = models.DateField("Дата выдачи задания", default=datetime.today)
    due_date = models.DateField("Дата сдачи задания")

    def __str__(self):
        return f'{self.group.name} | {self.date} | {self.subject_teacher.subject}'

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Grades(models.Model):
    """Оценки"""
    student = models.ForeignKey(Students, verbose_name="Ученик", on_delete=models.CASCADE)
    subject_teacher = models.ForeignKey(SubjectsTeachers, verbose_name='Предмет и преподаватель',
                                        on_delete=models.CASCADE)
    teachers_comment = models.TextField(verbose_name="Комментарий преподавателя", null=True, blank=True)
    date = models.DateField("Дата проставления оценки", default=date.today)
    grade = models.IntegerField(
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f'{self.student.credentials.fio} | {self.subject_teacher.subject} | ' \
               f'{self.grade} | {self.date}'

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class StudentsAnswers(models.Model):
    """Ответы на задния"""
    student = models.ForeignKey(Students, verbose_name="Студент", on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, verbose_name="Задание", on_delete=models.CASCADE)
    answer = models.FileField(verbose_name="Ответ ученика")
    grade = models.ForeignKey(Grades, verbose_name="Оценка", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.credentials.fio} | {self.task.subject_teacher.subject} | ' \
               f'{self.task.date}'

    class Meta:
        verbose_name = "Ответ на задание"
        verbose_name_plural = "Ответы на задание"
