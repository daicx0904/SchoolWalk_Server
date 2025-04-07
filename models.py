from django.contrib.gis.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    courses = models.ManyToManyField("Course")


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    office_location = models.PointField(srid=4326)
    courses = models.ManyToManyField("Course")


class Course(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.JSONField()  # 存储时间安排
    classroom = models.CharField(max_length=50)
