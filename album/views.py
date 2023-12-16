from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import AlbumModel
from .forms import AlbumForm

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = AlbumModel
    template_name = 'album/index.html'
    form_class = AlbumForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = AlbumModel
    template_name = 'album/index.html'
    form_class = AlbumForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(View):
    def get(self, request, pk):
        album = AlbumModel.objects.get(pk=pk)
        album.delete()
        return redirect('home')