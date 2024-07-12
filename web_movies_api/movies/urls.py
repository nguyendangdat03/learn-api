from django.urls import path
from .views import MovieListCreate, MovieDetail, index, StudentIdAPIView, StudentBirthDayAPIView, StudentAgeAPIView, ObtainTokenAndStudentName

urlpatterns = [
    path('', index, name='index'),
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies/students/', StudentIdAPIView.as_view(), name='student-id-api'),
    path('movies/students/birth_day/', StudentBirthDayAPIView.as_view(), name='student-birth-day-api'),
    path('movies/students/age/', StudentAgeAPIView.as_view(), name='student-age-api'),
    path('movies/students/token_and_name/', ObtainTokenAndStudentName.as_view(), name='obtain-token-and-student-name'),
]
