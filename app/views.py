from django.shortcuts import render

# Create your views here.
def honey(request):
    d={'a':100,'b':234,'c':200}
    return render(request,'honey.html',d)
