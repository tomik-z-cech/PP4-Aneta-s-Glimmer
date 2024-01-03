# PEP8
# Imports
from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from django.db.models import Count, Q
from news.models import NewsPosts
from styles.models import StylesAvailable
from artists.models import Artists
from bookings.models import Bookings
from landing.forms import SearchBarForm


class LandingPageView(generic.ListView):
    """
    Class generates view landing page
    """

    template_name = "landing/index.html"

    def get(self, request, *args, **kwargs):
        """This method generates view of landing page"""
        # Init search form
        search_form = SearchBarForm()
        # Select 3 newest newst posts
        # Only if they are published
        # Annotate amount of comments
        news = NewsPosts.objects.annotate(
            comments_num=Count("news_comments", filter=Q(
                news_comments__approved=1))
        ).filter(is_published=1)[:3]
        # Select 3 top styles by likes
        # Annotate number of likes
        top_styles_like = StylesAvailable.objects.annotate(
            likes_num=Count("likes")
        ).order_by("-likes_num")[:3]
        # Select 3 top tries styles
        # Annotate number of tries
        top_styles_try = StylesAvailable.objects.annotate(
            want_to_try_num=Count("want_to_try")
        ).order_by("-want_to_try_num")[:3]
        # Select all artists
        artists = Artists.objects.all()
        # Initialize empty string for top artists
        top_artists_all = []
        # For each artist, count the rating score
        for artist in artists:
            valid_bookings_count = 0
            rating_total = 0
            # Filter all rated bookings for each artist
            valid_bookings = Bookings.objects.filter(is_rated=True).filter(
                booked_artist=artist.id
            )
            # For each rated booking
            for valid_booking in valid_bookings:
                # Increase counter
                valid_bookings_count = valid_bookings_count + 1
                # increase running score
                rating_total = rating_total + valid_booking.rating
            # If any rated bookings
            if valid_bookings_count != 0:
                # Count rating
                rating = rating_total / valid_bookings_count
                # Append to array
                top_artists_all.append(
                    {
                        "name": artist.name,
                        "rating": rating,
                        "rating_count": valid_bookings_count,
                        "slug": artist.slug,
                    }
                )
                # Sort and slice top artists, 3 tops
                top_artists = sorted(
                    top_artists_all, key=lambda x: x["rating"], reverse=True
                )[:3]
        # Render tamplate
        return render(
            request,
            self.template_name,
            {
                "news_list": news,
                "top_styles_like": top_styles_like,
                "top_styles_try": top_styles_try,
                "top_artists": top_artists,
                "search_form": search_form,
            },
        )

    def search(request):
        """
        Search method - returns template with results
        """
        search_form = SearchBarForm(request.GET)
        # Search in following objects - all
        artists = Artists.objects.all()
        news = NewsPosts.objects.all()
        styles = StylesAvailable.objects.all()
        # If form valid
        if search_form.is_valid():
            search_query = search_form.cleaned_data.get("search_query")
            # Return results
            if search_query:
                news_results = news.filter(title__icontains=search_query)
                artists_results = artists.filter(name__icontains=search_query)
                styles_results = styles.filter(
                    style_name__icontains=search_query)
        # Render template with results
        return render(
            request,
            "landing/search_results.html",
            {
                "styles_results": styles_results,
                "news_results": news_results,
                "artists_results": artists_results,
                "search_form": search_form,
            },
        )
