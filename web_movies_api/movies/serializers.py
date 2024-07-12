from rest_framework import serializers
from .models import Movie
from .models import Student

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id']
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id']
        