from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import  login_required
#from .models import Contrato
#from .forms import ContratoForm
from .models import Contrato
from .forms import ContratoForm
