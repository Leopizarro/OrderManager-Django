from django.shortcuts import render, redirect
from .forms import PedidoForm
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def pedido_create_view(request, uid, pid):
    user = request.user.id
    product = Product.objects.get(id=pid)
    form = PedidoForm({'comprador_id':uid, 'product_id':pid})

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../../products/')

    context = {
        'form': form,
        'product': product
    }
    return render(request, "pedidos/pedido_create.html",context)
