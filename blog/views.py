from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from.models import Publicar
def listar(request):
    publi=Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar.html',{'publi':publi})
def detalle_pub(request,pk):
    p=get_object_or_404(Publicar,pk=pk)
    return render(request, 'blog/detalle_pub.html',{'p':p})
# Create your views here.
