from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StudentForm
from .models import Student


# Create your views here.
def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/create.html',
        {'form': form}
    )  

def student_list(request):
    student = Student.objects.all()

    return render(
        request,
        'students/list.html',
        {'students': student}
    )

def student_update(request, pk):

    student = Student.objects.get(id=pk)

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(
        request,
        'students/update.html',
        {'form': form}
    )
    
def student_delete(request,pk):

    student = Student.objects.get(
        id=pk
    )

    student.delete()

    return redirect(
        'student_list'
    )