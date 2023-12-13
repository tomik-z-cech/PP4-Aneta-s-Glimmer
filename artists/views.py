from django.shortcuts import render
from django.views import generic
from artists.models import Artists
from styles.models import StylesAvailable
from bookings.models import Bookings

# ----------------------- TEAM VIEWS --------------------- #


class TeamView(generic.ListView):
    template_name = "artists/artists.html"
    def get(self, request, *args, **kwargs):
        artists = Artists.objects.all()
        artists_to_send = []
        for artist in artists:
            valid_bookings_count = 0
            rating_total = 0
            valid_bookings = Bookings.objects.filter(is_rated=True).filter(
                booked_artist=artist.id
            )
            for valid_booking in valid_bookings:
                valid_bookings_count = valid_bookings_count + 1
                rating_total = rating_total + valid_booking.rating
                rating = rating_total / valid_bookings_count
            if valid_bookings_count == 0:
                rating = 0
            artists_to_send.append(
                {
                    "artist": artist,
                    "rating": rating,
                    "rating_count": valid_bookings_count,
                }
            )
        return render(
            request,
            self.template_name,
            {
                "artists_list": artists_to_send,
            },
        )


class TeamDetailView(generic.DetailView):
    template_name = "artists/artist_detail.html"
    model = Artists
    slug_field = "slug"

    def get(self, request, *args, **kwargs):
        artist_selected = self.get_object()
        styles_this_artist = StylesAvailable.objects.filter(
            artists__in=[artist_selected]
        )
        style_slug = styles_this_artist.values_list("slug", flat=True)
        filtered_styles = zip(style_slug, styles_this_artist)
        valid_bookings_count = 0
        rating_total = 0
        valid_bookings = Bookings.objects.filter(is_rated=True).filter(
                booked_artist=artist_selected.id
            )
        for valid_booking in valid_bookings:
            valid_bookings_count = valid_bookings_count + 1
            rating_total = rating_total + valid_booking.rating
            rating = rating_total / valid_bookings_count
        if valid_bookings_count == 0:
                rating = 0
        print(rating, valid_bookings_count)
        return render(
            request,
            self.template_name,
            {
                "name": artist_selected.name,
                "profile_picture": artist_selected.profile_picture,
                "bio": artist_selected.bio,
                "public_profile": artist_selected.public_profile,
                "start_date": artist_selected.start_date,
                "filtered_styles": filtered_styles,
                "rating": rating,
                "bookings_total": valid_bookings_count
                
            },
        )
