from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from news.models import NewsPosts, NewsComments
from news.forms import NewsCommentForm

# ----------------------- NEWS --------------------- #
class AllNewsView(generic.ListView):
    template_name = 'news/all_news.html'
    def get(self, request, *args, **kwargs):
        news = NewsPosts.objects.annotate(comments_num=Count('news_comments', filter=Q(news_comments__approved=1))).filter(is_published=1)
        return render(request, self.template_name, {
            "news_list": news,
        })

class NewsDetailView(generic.DetailView):
    template_name = 'news/news_detail.html'
    def get(self, request, slug, *args, **kwargs):
        search_query = NewsPosts.objects.filter(is_published=1)
        post = get_object_or_404(search_query, slug=slug)
        comments = NewsComments.objects.filter(approved=True).filter(post__in=[post]).order_by('created_on')
        users_liked = post.likes.all()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            self.template_name,
            {
                "news_detail": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "news_comment_form": NewsCommentForm(),
                "users_liked": users_liked,
            },
        )
    def post(self, request, slug, *args, **kwargs):
        search_query = NewsPosts.objects.filter(is_published=1)
        post = get_object_or_404(search_query, slug=slug)
        comments = NewsComments.objects.filter(approved=True).filter(post__in=[post]).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        news_comment_form = NewsCommentForm(data=request.POST)
        if news_comment_form.is_valid():
            news_comment_form.instance.username = request.user
            new_comment = news_comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            news_comment_form = NewsCommentForm() 
        return render(
            request,
            self.template_name,
            {
                "news_detail": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "news_comment_form": NewsCommentForm(),
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
    

