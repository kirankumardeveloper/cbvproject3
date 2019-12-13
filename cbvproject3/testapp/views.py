from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')

class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo','location')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy("companies")
