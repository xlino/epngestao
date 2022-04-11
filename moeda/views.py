from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import  login_required
#from .models import Contrato
#from .forms import ContratoForm
from .models import Contrato
from .forms import ContratoForm
import locale

# Create your views here.
#def listamoeda(request):
#    return render(request, 'moeda.html', {'valor': (444)})

    #def get_context_data(self, **kwargs:Any) -> Dict[str, Any]:
       #return {
           #"valor": 333
       #}

def teste(request):
    return render(request, 'teste.html')

@login_required
def listamoeda(request):
    form = ContratoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'moeda.html', {'form': form})
