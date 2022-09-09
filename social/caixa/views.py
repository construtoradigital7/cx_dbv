from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pedidos
from .forms import ComidaForm

#def post_list(request):
#    posts = Pedidos.objects.all()
#    return render(request, 'caixa/post_list.html', {'posts': posts})

def post_new(request):
     if request.method == "POST":
         form = ComidaForm(request.POST)
         if form.is_valid():
             post = form
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = ComidaForm()
     return render(request, 'caixa/post_edit.html', {'form': form})


def post_list(request):
    posts = Pedidos.objects.all()
    template = loader.get_template('caixa/post_list.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))
