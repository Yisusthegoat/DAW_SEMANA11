from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from .models import Producto


def home(request):
    """Página inicial con un resumen breve del catálogo."""
    contexto = {
        "fecha_actual": timezone.localdate(),
        "total_productos": Producto.objects.count(),
        "productos_destacados": Producto.objects.order_by("-fecha_registro", "nombre")[:3],
    }
    return render(request, "home.html", contexto)


class CatalogoListView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["total_productos"] = self.get_queryset().count()
        contexto["productos_disponibles"] = Producto.objects.filter(stock__gt=0).count()
        contexto["fecha_actual"] = timezone.localdate()
        return contexto
