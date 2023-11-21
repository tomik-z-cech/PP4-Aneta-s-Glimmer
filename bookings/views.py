from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic,View
from .models import NewsPosts

class NewsList(generic.ListView):
    model = NewsPosts
    result = NewsPosts.objects.filter(is_published=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'news_list'

