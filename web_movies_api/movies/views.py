from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie, Student
from .serializers import MovieSerializer, StudentSerializer
from datetime import date

# Existing Movie Views
class MovieListCreate(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        movie_id = self.request.query_params.get('id', None)
        if movie_id is not None:
            queryset = queryset.filter(id=movie_id)
        return queryset

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def index(request):
    return render(request, 'index.html')

# New View to Obtain Token and Student Name
class ObtainTokenAndStudentName(APIView):
    def post(self, request):
        student_id = request.data.get('id')
        
        try:
            student = Student.objects.get(id=student_id)
            refresh = RefreshToken.for_user(student)
            
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'name': student.name
            }
            return Response(data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

# Existing Student Views
class StudentIdAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_id = request.GET.get('id')
        
        try:
            student = Student.objects.get(id=student_id)
            return Response({'id': student.id})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

class StudentBirthDayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_id = request.GET.get('id')
        
        try:
            student = Student.objects.get(id=student_id)
            data = {
                'id': student.id,
                'name': student.name,
                'date_of_birth': student.date_of_birth.strftime('%Y-%m-%d')
            }
            return Response(data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        
class StudentAgeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_id = request.GET.get('id')
        
        try:
            student = Student.objects.get(id=student_id)
            today = date.today()
            age = today.year - student.date_of_birth.year - ((today.month, today.day) < (student.date_of_birth.month, student.date_of_birth.day))
            return Response({'id': student.id, 'name': student.name, 'age': age})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
