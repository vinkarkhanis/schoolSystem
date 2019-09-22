from django.shortcuts import render
from .models import Student
from tablib import Dataset
from .resources import StudentResource


def index(request):
    dests = Student.objects.all()

    return render(request, 'index.html', {'dests': dests})

def simple_upload(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read())
        result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')