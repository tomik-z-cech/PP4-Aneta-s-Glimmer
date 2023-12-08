from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.db.models import Count
from django.http import HttpResponseRedirect
from news.models import NewsPosts, NewsComments

# ----------------------- NEWS --------------------- #
class AllNewsView(generic.ListView):
    template_name = 'news/all_news.html'
    def get(self, request, *args, **kwargs):
        news = NewsPosts.objects.annotate(comments_num=Count('news_comments')).filter(is_published=1)
        
        return render(request, self.template_name, {
            "news_list": news,
        })

class NewsDetailView(generic.DetailView):
    template_name = 'news/news_detail.html'
    def get(self, request, slug, *args, **kwargs):
        search_query = NewsPosts.objects.filter(is_published=1)
        post = get_object_or_404(search_query, slug=slug)
        comments = NewsComments.objects.filter(approved=True).filter(post__in=[post]).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        print(liked)
        return render(
            request,
            self.template_name,
            {
                "news_detail": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                # "comment_form": CommentForm(),
            },
        )
        
class NewsPostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(NewsPosts, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('news-detail', args=[slug]))
    
