from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import MusicianModel
from .forms import MusicianForm

@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = MusicianModel
    template_name = 'musician/index.html'
    form_class = MusicianForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = MusicianModel
    template_name = 'musician/index.html'
    form_class = MusicianForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(View):
    def get(self, request, pk):
        album = MusicianModel.objects.get(pk=pk)
        album.delete()
        return redirect('home')
