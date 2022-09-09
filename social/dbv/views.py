from django.views import generic
from .models import Bebida, Lanche


class IndexView(generic.ListView):
    template_name = 'dbv/cadastro_pedido.html'
    context_object_name = 'lista'


    def get_queryset(self):
        return (Lanche.objects.order_by('descricao'), Bebida.objects.order_by('descricao'))
