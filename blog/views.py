from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar
from .forms import postearForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def listar(request):
    publi=Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar.html',{'publi':publi})

def detalle_pub(request, pk):
    p=get_object_or_404(Publicar,pk=pk)
    return render(request, 'blog/detalle_pub.html', {'p':p})
@login_required
def nueva_publicacion(request):
    if request.method == "POST":
        f = postearForms(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            #p.fecha_publica = timezone.now()
            p.save()
            return redirect('postear', pk=p.pk)
    else:
        f = postearForms()
    return render(request, 'blog/nueva_publicacion.html', {'f': f})

def editar_publicacion(request,pk):
    p=get_object_or_404(Publicar ,pk=pk)
    if request.method=="POST":
        f=postearForms(request.POST, instance=p)
        if f.is_valid():
            p=f.save(commit=False)
            p.autor=request.user
            p.save()
            # return redirect('detalle_pub',pk=p.pk)
            return render(request, 'blog/detalle_pub.html', {'p':p})
    else:
        f=postearForms(instance=p)
        return render(request,'blog/nueva_publicacion.html', {'f':f})

def post_draft_list(request):
    posts = Publicar.objects.filter(fecha_publica__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Publicar, pk=pk)
    post.publicacion()
    return redirect('postear', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Publicar, pk=pk)
    post.delete()
    return redirect('listar')



# Create your views here.
