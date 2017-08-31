from django.shortcuts import render
from django.utils import timezone
from.models import Publicar
def listar(request):
    publi=Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar.html',{'publi':publi})
# Create your views here.
