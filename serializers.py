from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    office_location = serializers.JSONField(
        source="office_location.coords", read_only=True
    )

    class Meta:
        model = Teacher
        fields = "__all__"
