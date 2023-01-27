from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from templating.models import Items, Blog


def increase_views(request, pk, slug):
    blog_items = get_object_or_404(Blog, pk=pk, slug=slug)
    blog_items.view += 1
    blog_items.save()
    return redirect(reverse(f'templating:blog_detail/{str(pk)}/{slug}/'))


class BlogListView(ListView):
    model = Blog


class HomeListView(ListView):
    model = Items


class BlogCreateView(CreateView):
    model = Blog
    fields = ('heading', 'content', 'image')
    success_url = reverse_lazy('templating:blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'content', 'image', 'status')
    success_url = reverse_lazy('templating:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('templating:blog')


class BlogDetailView(DetailView):
    model = Blog
    fields = ('heading', 'content', 'image')


def contacts_page(request):
    return render(request, 'templating/contacts.html')

