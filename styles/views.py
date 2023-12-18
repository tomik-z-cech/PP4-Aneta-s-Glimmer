from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.db.models import Count, Q
from styles.models import StylesAvailable
from artists.models import Artists


# ----------------------- STYLES VIEWS --------------------- #


class StylesView(generic.ListView):
    template_name = "styles/styles.html"
    
    def get(self, request, *args, **kwargs):
        # Select all news
        styles_list = StylesAvailable.objects.annotate(comments_num=Count("style_comments", filter=Q(style_comments__approved=1))).all()
        # Render template and send news
        return render(
            request,
            self.template_name,
            {
                "styles_list": styles_list,
            },
        )


class StyleDetailView(generic.DetailView):
    template_name = "styles/style_detail.html"
    model = StylesAvailable
    slug_field = "slug"
    context_object_name = "style_detail"

    def get(self, request, *args, **kwargs):
        style_selected = self.get_object()
        artists_with_style = Artists.objects.filter(styles__in=[style_selected])
        artists_slug = artists_with_style.values_list("slug", flat=True)
        filtered_artists = zip(artists_slug, artists_with_style)
        users_liked_styles = style_selected.likes.all()
        users_want_to_try_styles = style_selected.want_to_try.all()
        liked = False
        if style_selected.likes.filter(id=self.request.user.id).exists():
            liked = True
        want_to_try = False
        if style_selected.want_to_try.filter(id=self.request.user.id).exists():
            want_to_try = True
        return render(
            request,
            self.template_name,
            {
                "style_name": style_selected.style_name,
                "style_description": style_selected.style_description,
                "sample_image": style_selected.sample_image,
                "likes": style_selected.number_of_likes,
                "tries": style_selected.number_of_tries,
                "slug": style_selected.slug,
                "filtered_artists": filtered_artists,
                "liked": liked,
                "want_to_try": want_to_try,
                "users_liked": users_liked_styles,
                "users_want_to_try": users_want_to_try_styles
            },
        )
        
class StyleLike(LoginRequiredMixin, View):
    def post(self, request, slug):
        style = get_object_or_404(StylesAvailable, slug=slug)
        
        if style.likes.filter(id=request.user.id).exists():
            style.likes.remove(request.user)
        else:
            style.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('style-detail', args=[slug]))
    
class StyleTry(LoginRequiredMixin, View):
    def post(self, request, slug):
        style = get_object_or_404(StylesAvailable, slug=slug)
        
        if style.want_to_try.filter(id=request.user.id).exists():
            style.want_to_try.remove(request.user)
        else:
            style.want_to_try.add(request.user)
        
        return HttpResponseRedirect(reverse('style-detail', args=[slug]))
