from .models import Student
from rest_framework import serializers
from comman.constants import MAX_STUDENT_AGE
from comman.enums import Grades


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    grade = serializers.ChoiceField(choices=[g.value for g in Grades])

    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def validate_age(self, value: int) -> int:
        if value > MAX_STUDENT_AGE:
            raise serializers.ValidationError(f"Age cannot exceed {MAX_STUDENT_AGE}.")
        return value


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"

#     def validate_age(self, value: int) -> int:
#         if value > MAX_STUDENT_AGE:
#             raise serializers.ValidationError(f"Age cannot exceed {MAX_STUDENT_AGE}.")
#         return value
