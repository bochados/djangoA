from django.shortcuts import render
def listar(request):
    return render(request,'blog/listar.html',{})
# Create your views here.
