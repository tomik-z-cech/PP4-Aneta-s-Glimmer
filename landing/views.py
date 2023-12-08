from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from news.models import NewsPosts
from styles.models import StylesAvailable
from artists.models import Artists

# ----------------------- LANDING PAGE --------------------- #
class LandingPageView(generic.ListView):
    """
    Class generates view of all news posts for landing page
    """
    template_name = 'landing/index.html'
    def get(self, request, *args, **kwargs):
        news = NewsPosts.objects.annotate(comments_num=Count('news_comments')).filter(is_published=1)[:3]
        top_styles_like = StylesAvailable.objects.annotate(likes_num=Count('likes')).order_by('-likes_num')[:3]
        top_styles_try = StylesAvailable.objects.annotate(want_to_try_num=Count('want_to_try')).order_by('-want_to_try_num')[:3]
        top_artists = Artists.objects.all().order_by('-rating')[:3]
        return render(request, self.template_name, {
            "news_list": news,
            "top_styles_like": top_styles_like,
            "top_styles_try": top_styles_try,
            "top_artists": top_artists,
        })
