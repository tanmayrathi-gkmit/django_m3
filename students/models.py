from django.db import models
from comman.enums import Grades


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    grade = models.CharField(
        max_length=20, choices=[(_grade.value, _grade.value) for _grade in Grades]
    )
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.grade})"
