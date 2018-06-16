from django.shortcuts import render
from django.views import generic
from .models import Instructor, Student, Attendance, Progress, Fee, Batch, Enrollment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime

# Index Page
def index(request):
    instructor = Instructor.objects.get(id=1)
    return render(request, 'student/index.html', context={'instructor': instructor})

# Student Index Page
class StudentIndexView(generic.ListView):
    template_name = 'student/student.html'

    def get_queryset(self):
        return Student.objects.all()

# Student Detail Page
def studentdetail(request, pk):
    student_detail = Student.objects.get(pk=pk)
    guardian_detail = student_detail.guardian
    attendance_detail = Attendance.objects.filter(student=pk)
    progress_detail = Progress.objects.filter(student=pk)
    fee_detail = Fee.objects.filter(student=pk)
    context = {
        'stu': student_detail,
        'guardian': guardian_detail,
        'attendance': attendance_detail,
        'progress':  progress_detail,
        'fee': fee_detail,
    }
    return render(request, 'student/detail.html', context)

# Student Update Pages
class StudentCreate(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank']

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank']

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Batch Information Pages
def batch(request):
    batches = Batch.objects.all()
    context = {
        'batches': batches,
        }
    return render(request, 'student/batch.html', context)

# Students in given Batch
def batchstudent(request, pk):
    enrolls = Enrollment.objects.filter(batch=pk)
    students = []
    for enroll in enrolls:
        students.append(enroll.student)
    return render(request, 'student/student.html', { 'object_list': students })

# Add Attendance
def StudentAddAttendance(request, pk):
    enrolls = Enrollment.objects.filter(batch=pk)
    student_id = []
    flag = 0
    for enroll in enrolls:
        student_id.append(enroll.student.pk)
    for id in student_id:
        attend = Attendance.objects.filter(student=id).filter(attendance_month=datetime.today().strftime('%B')).filter(attendance_year = datetime.today().strftime('%Y'))
        if attend:
            attend.attendance_count += 1
            attend.save()
            flag = 1
        else:
            new_attendance = Attendance(attendance_month = datetime.today().strftime('%B'), attendance_year = datetime.today().strftime('%Y'), attendance_count = 1)
            new_attendance.save()
            flag = 1
    return render(request, reverse_lazy('student:batch'), {'count': len(student_id)})

# Finance Page
def finance(request):
    all_fees = Fee.objects.all().order_by('student')
    return render(request, 'student/finance.html', {'all_fees': all_fees})
