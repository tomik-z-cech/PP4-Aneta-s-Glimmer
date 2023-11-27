from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Count
from .models import NewsPosts, StylesAvailable, Artists, UserProfile, User, NewsComments
from .forms import UpdateDetailsForm

# ----------------------- LANDING PAGE --------------------- #
class LandingPageView(generic.ListView):
    """
    Class generates view of all news posts for landing page
    """
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        news = NewsPosts.objects.annotate(comments_num=Count('news_comments')).filter(is_published=1)
        top_styles_like = StylesAvailable.objects.annotate(likes_num=Count('likes')).order_by('-likes_num')[:3]
        top_styles_try = StylesAvailable.objects.annotate(want_to_try_num=Count('want_to_try')).order_by('-want_to_try_num')[:3]
        top_artists = Artists.objects.all().order_by('-rating')[:3]
        
        return render(request, self.template_name, {
            "news_list": news,
            "top_styles_like": top_styles_like,
            "top_styles_try": top_styles_try,
            "top_artists": top_artists,
        })

# ----------------------- NEWS --------------------- #
class AllNewsView(generic.ListView):
    template_name = 'all_news.html'
    def get(self, request, *args, **kwargs):
        news = NewsPosts.objects.annotate(comments_num=Count('news_comments')).filter(is_published=1)
        
        return render(request, self.template_name, {
            "news_list": news,
        })

class NewsDetailView(generic.DetailView):
    template_name = 'news_detail.html'
    def get(self, request, slug, *args, **kwargs):
        search_query = NewsPosts.objects.filter(is_published=1)
        post = get_object_or_404(search_query, slug=slug)
        comments = NewsComments.objects.filter(approved=True).filter(post__in=[post]).order_by('created_on')
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
                # "comment_form": CommentForm(),
            },
        )
# ----------------------- STYLES VIEWS --------------------- #
    
class StylesView(generic.ListView):
    model = StylesAvailable
    queryset = StylesAvailable.objects.all()
    template_name = 'styles.html'
    context_object_name = 'styles_list'

class StyleDetailView(generic.DetailView):
    template_name = 'style_detail.html'
    model = StylesAvailable
    slug_field = 'slug'
    context_object_name = 'style_detail'
    def get(self, request, *args, **kwargs):
        style_selected = self.get_object()
        artists_with_style = Artists.objects.filter(styles__in=[style_selected])
        artists_slug = artists_with_style.values_list('slug', flat=True)
        filtered_artists = zip(artists_slug, artists_with_style)
        return render(request, self.template_name, {
            "style_name": style_selected.style_name,
            "style_description" : style_selected.style_description,
            "sample_image": style_selected.sample_image,
            "likes": style_selected.number_of_likes,
            "tries": style_selected.number_of_tries,
            "filtered_artists": filtered_artists,
        })
        
# ----------------------- TEAM VIEWS --------------------- # 

class TeamView(generic.ListView):
    model = Artists
    queryset = Artists.objects.all()
    template_name = 'artists.html'
    context_object_name = 'artists_list'

class TeamDetailView(generic.DetailView):
    template_name = 'artist_detail.html'
    model = Artists
    slug_field = 'slug'
    def get(self, request, *args, **kwargs):
        artist_selected = self.get_object()
        styles_this_artist = StylesAvailable.objects.filter(artists__in=[artist_selected])
        style_slug = styles_this_artist.values_list('slug', flat=True)
        filtered_styles = zip(style_slug, styles_this_artist)
        return render(request, self.template_name, {
            "name": artist_selected.name,
            "profile_picture": artist_selected.profile_picture,
            "bio": artist_selected.bio,
            "public_profile": artist_selected.public_profile,
            "start_date": artist_selected.start_date,
            "rating": artist_selected.rating,
            "bookings_total": artist_selected.bookings_total,
            "filtered_styles": filtered_styles
        })
        
# ----------------------- MY PROFILE VIEWS --------------------- #
class MyDetailsView(generic.ListView):
    template_name = 'my_details.html'
    model = UserProfile
    def get(self, request, *args, **kwargs):
        login_user = request.user
        profile_selected = login_user.userprofile
        details_form = UpdateDetailsForm(instance=profile_selected)
        return render(request, self.template_name,{
            'details_form': details_form,
            'username': login_user.username
            })
    def post(self, request, *args, **kwargs):
        updated_profile = request.user.userprofile
        form = UpdateDetailsForm(request.POST, instance=updated_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        
class DeleteMyProfileView(generic.ListView):
    def get(self, request, *args, **kwargs):
        model = User
        logged_in_user = request.user
        logged_in_user.delete()
        return redirect('home')