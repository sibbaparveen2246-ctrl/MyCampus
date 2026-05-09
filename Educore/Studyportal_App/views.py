from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request,'Studyportal_App/home.html')




def add_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        Student.objects.create( name=name, phone_no=phone_no, subject=subject, email=email)

        messages.success(request,'Student Added Successfully!')
        return redirect('add')

    return render(request,'Studyportal_App/add.html')


def search_student(request):

    student = []
    message = ''

    if request.method == 'POST':
        choose = request.POST.get('choose')

        if choose == 'Search_ID':
            student_id = request.POST.get('id')

            if student_id:
                student = Student.objects.filter(id = student_id)

                if student:
                    message = 'Record Found!'
                else:
                    message = 'Record Not Found!'

            else:
                message = 'Invalid Id!'
        
        elif choose == 'Search_All':
            student = Student.objects.all()
            message = 'List of Student'

    return render(request,'StudyPortal_App/search.html',{'student':student, 'message':message})

        
def update_student(request):
    
    if request.method == 'POST':
        student_id = request.POST.get('id')

        if not student_id:
            messages.error(request,"Enter Student Id")
            return redirect('update')

        try:
            record = Student.objects.get(id = student_id)

            name = request.POST.get('name')
            phone_no = request.POST.get('phone_no')
            subject = request.POST.get('subject')
            email = request.POST.get('email')

            if name: 
                record.name = name
            if phone_no:
                record.phone_no = phone_no
            if subject:
                record.subject = subject
            if email:
                record.email = email

            record.save()
            messages.success(request,"Student Record Updated!")

        except Student.DoesNotExist:
            messages.error(request,"Student Not Found!")
        return redirect('update')

    return render(request,'Studyportal_App/update.html')


def delete_student(request):

    students = []
    message = ''

    if request.method == 'POST':
        choose = request.POST.get('choose')

        if choose == 'Delete_ID':
            student_id = request.POST.get('id')

            if not student_id :
                message = 'Enter Student Id'

            else:
                try:
                    students = Student.objects.get(id = student_id)
                    students.delete()
                    message = "Student Deleted!"

                except:
                    message = 'Invalid Student Id'

            students = Student.objects.all()

        elif choose == 'Delete_All':
            Student.objects.all().delete()
            students = []
            message = "All Student Deleted!"

    return render(request,'Studyportal_App/delete.html',{'students':students, 'message':message})
