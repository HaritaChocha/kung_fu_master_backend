from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    # Index Page
    path('', views.index, name='index'),

    # Student Pages
    path('student/', views.StudentIndexView.as_view(), name='student'),
    path('student/add', views.StudentCreate.as_view(), name="student-add"),
    path('student/update/<pk>', views.StudentUpdate.as_view(), name="student-update"),
    path('student/delete/<pk>', views.StudentDelete.as_view(), name="student-delete"),
    path('student/<pk>', views.studentdetail, name='detail'),

    # Batch Pages
    path('batch/', views.batch, name='batch'),
    path('batch/<pk>/students', views.batchstudent, name='batch_student'),
    path('batch/<pk>/attendance', views.StudentAddAttendance, name='attendance'),

    # Finance Pages
    path('finance/', views.finance , name='finance'),
]