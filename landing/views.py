from django.shortcuts import render
from django.views import generic
from django.db.models import Count, Q
from news.models import NewsPosts
from styles.models import StylesAvailable
from artists.models import Artists
from bookings.models import Bookings
from landing.forms import SearchBarForm


# ----------------------- LANDING PAGE --------------------- #
class LandingPageView(generic.ListView):
    """
    Class generates view of all news posts for landing page
    """

    template_name = "landing/index.html"

    def get(self, request, *args, **kwargs):
        search_form = SearchBarForm()
        news = NewsPosts.objects.annotate(
            comments_num=Count("news_comments", filter=Q(news_comments__approved=1))
        ).filter(is_published=1)[:3]
        top_styles_like = StylesAvailable.objects.annotate(
            likes_num=Count("likes")
        ).order_by("-likes_num")[:3]
        top_styles_try = StylesAvailable.objects.annotate(
            want_to_try_num=Count("want_to_try")
        ).order_by("-want_to_try_num")[:3]
        artists = Artists.objects.all()
        top_artists_all = []
        for artist in artists:
            valid_bookings_count = 0
            rating_total = 0
            valid_bookings = Bookings.objects.filter(is_rated=True).filter(booked_artist=artist.id)
            for valid_booking in valid_bookings:
                valid_bookings_count = valid_bookings_count + 1
                rating_total = rating_total + valid_booking.rating
            if valid_bookings_count != 0:
                rating = rating_total / valid_bookings_count
                top_artists_all.append({"name": artist.name, "rating": rating, "rating_count": valid_bookings_count, "slug": artist.slug})
                top_artists = sorted(top_artists_all, key=lambda x: x['rating'], reverse=True)[:3]
        return render(
            request,
            self.template_name,
            {
                "news_list": news,
                "top_styles_like": top_styles_like,
                "top_styles_try": top_styles_try,
                "top_artists": top_artists,
                "search_form": search_form
            },
        )
    

    def search(request):
        search_form = SearchBarForm(request.GET)
        artists = Artists.objects.all()

        if search_form.is_valid():
            search_query = search_form.cleaned_data.get('search_query')
            if search_query:
                artists_result = artists.filter(name__icontains=search_query)
        else:
            print('not valid')
        return render(request, 'landing/search_results.html', {'artists_results': artists_result, 'search_form': search_form})
