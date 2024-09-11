# student/views.py

from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')




# View for the 'About' page (Geethanjali Institute of Science and Technology)
def about(request):
  return render(request, 'about.html')  # Rendering the about.html template



# View for the 'Contact' page
def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        section = request.POST.get('section')
        branch = request.POST.get('branch')
        technical_skills = request.POST.get('skills')
        cgpa = request.POST.get('cgpa')
        mobile = request.POST.get('mobile')
        joining_year = request.POST.get('joining_year')

        # Save data to the database
        student = Student(
            name=name, student_id=student_id, section=section, branch=branch,
            technical_skills=technical_skills, cgpa=cgpa, mobile=mobile,
            joining_year=joining_year
        )
        student.save()

        # Pass a success message
        return render(request, 'register.html', {'success': True})
    else:
        return render(request, 'register.html')
    



def student_database(request):
    students = Student.objects.all()  # Fetch all students from the database

    # If filtering by CGPA is needed, you can use query parameters (optional)
    query = request.GET.get('q')
    if query:
        students = students.filter(name__icontains=query)

    return render(request, 'student_database.html', {'students': students})


def student_database(request):
    students = Student.objects.all()
    
    # Get the search query from the request
    query = request.GET.get('search')
    if query:
        students = students.filter(name__icontains=query) | students.filter(student_id__icontains=query)

    return render(request, 'student_database.html', {'students': students})
def student_database(request):
    students = Student.objects.all()

    # Handle search by name or student ID
    search_query = request.GET.get('search')
    if search_query:
        students = students.filter(name__icontains=search_query) | students.filter(student_id__icontains=search_query)

    # Handle filtering by CGPA
    cgpa_filter = request.GET.get('cgpa')
    if cgpa_filter:
        try:
            cgpa_filter = float(cgpa_filter)
            students = students.filter(cgpa__gte=cgpa_filter)
        except ValueError:
            pass  # Ignore invalid CGPA input

    return render(request, 'student_database.html', {'students': students})


