from django.urls import path
from .views import home, contract, about, student_list, student_create, student_update, student_delete

urlpatterns = [
    path('', home, name='home'),
    path('contract/', contract, name='contract'),
    path('about/', about, name='about'),
    path('students/', student_list, name='student_list'),
    path('students/create/', student_create, name='student_create'),
    path('students/update/<int:pk>/', student_update, name='student_update'),
    path('students/delete/<int:pk>/', student_delete, name='student_delete'),
]
