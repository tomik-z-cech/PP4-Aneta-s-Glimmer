from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import NewsPosts, StylesAvailable, Artists

class NewsList(generic.ListView):
    model = NewsPosts
    queryset = NewsPosts.objects.filter(is_published=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'news_list'

class NewsDetailView(generic.DetailView):
    model = NewsPosts
    slug_field = 'slug'
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    
class StylesView(generic.ListView):
    model = StylesAvailable
    queryset = StylesAvailable.objects.all()
    template_name = 'styles.html'
    context_object_name = 'styles_list'
    
class TeamView(generic.ListView):
    model = Artists
    queryset = Artists.objects.all()
    template_name = 'artists.html'
    context_object_name = 'artists_list'