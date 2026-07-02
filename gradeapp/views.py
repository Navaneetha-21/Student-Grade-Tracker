from django.shortcuts import render,redirect,get_object_or_404
from . form import GradeForm
from . models import GradeTrack


def home(request):
    students =GradeTrack.objects.all()
    if request.method == "POST":
        form=GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=GradeForm()

    count=students.count()
    class_average=0
    pass_rate=0
    for student in students:
        class_average=student.average+class_average
        if student.status=="pass":
            pass_rate=pass_rate+1

    if count>0:
        class_average /=count

        pass_per=(pass_rate/count)*100
    else:
        class_average=0
        pass_per=0   

    context={
        'form':form,
        'students':students,
        'total_students':count,
        'class_average':round(class_average,2),
        'pass_per':round(pass_per,2),
        
    }

    return render(request,'gradetemp/index.html',context)



def delete_view(request,id):
    delete_var = get_object_or_404(GradeTrack,id=id)
  
    delete_var.delete()
    return redirect('home')




