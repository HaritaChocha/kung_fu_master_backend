from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Instructor, Student, Attendance, Progress, Fee, Batch, Enrollment, Guardian
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from .form import *

# Index Page
def index(request):
    instructor = Instructor.objects.get(id=1)
    return render(request, 'student/index.html', context={'instructor': instructor})

# Instructor Page
class InstructorIndexView(generic.ListView):
    template_name = 'student/instructor.html'

    def get_queryset(self):
        return Instructor.objects.all()
        
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
    fields = ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank',
              'guardian']

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank',
              'guardian']

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# def guardian_create(request, pk):
#     form = GuardianForm(request.POST or None, request.FILES or None)
#     student = get_object_or_404(Student, pk=pk)
#     if form.is_valid():
#         # guardian = Student.guardian.all()
#         # for s in guardian:
#         #     if s.first_name == form.cleaned_data.get("first_name"):
#         #         context = {
#         #             'student': student,
#         #             'form': form,
#         #             'error_message': 'You already added that song',
#         #         }
#         #         return render(request, 'student/guardian_form.html', context)
#         guardian = form.save(commit=False)
#         student.guardian = guardian
#         guardian.save()
#         student.update()
#
#         return render(request, 'student/detail.html', {'stu': student})
#
#     context = {
#         'stu': student,
#         'form': form,
#     }
#     return render(request, 'student/guardian_form.html', context)

class GuardianCreate(CreateView):
    model = Guardian
    fields = ['first_name', 'last_name', 'address', 'city', 'phone_number', 'relation']

#Batch Information Pages
class BatchIndexView(generic.ListView):
    template_name = 'student/batch.html'

    def get_queryset(self):
        return Batch.objects.all()

class BatchCreate(CreateView):
    model = Batch
    fields = ['batch_day', 'batch_start_time', 'batch_end_time', 'level', 'instructor']

class BatchUpdate(UpdateView):
    model = Batch
    fields = ['batch_day', 'batch_start_time', 'batch_end_time', 'level', 'instructor']

class BatchDelete(DeleteView):
    model = Batch
    success_url = reverse_lazy('student:batch')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Students in given Batch
def batchstudent(request, pk):
    enrolls = Enrollment.objects.filter(batch=pk)
    students = []
    for enroll in enrolls:
        students.append(enroll.student)
    return render(request, 'student/student.html', { 'object_list': students })

# Attendance Page
class AttendanceIndexView(generic.ListView):
    template_name = 'student/attend.html'

    def get_queryset(self):
        return Attendance.objects.all()

class AttendanceCreate(CreateView):
    model = Attendance
    fields = ['student', 'attendance_date', 'attendance_count']

class AttendanceUpdate(UpdateView):
    model = Attendance
    fields = ['student', 'attendance_date', 'attendance_count']

class AttendanceDelete(DeleteView):
    model = Attendance
    success_url = reverse_lazy('student:attend')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Finance Page
class FinanceIndexView(generic.ListView):
    template_name = 'student/finance.html'

    def get_queryset(self):
        return Fee.objects.all()

class FinanceCreate(CreateView):
    model = Fee
    fields = ['fee_name', 'fee_date', 'fee_amount', 'student']

class FinanceUpdate(UpdateView):
    model = Fee
    fields = ['fee_name', 'fee_date', 'fee_amount']

class FinanceDelete(DeleteView):
    model = Fee
    success_url = reverse_lazy('student:finance')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def monthly_report(request):
    pass