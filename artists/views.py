# Imports
from django.shortcuts import render
from django.views import generic
from artists.models import Artists
from styles.models import StylesAvailable
from bookings.models import Bookings


class TeamView(generic.ListView):
    """
    Class renders view of all artists
    """

    template_name = "artists/artists.html"  # Template name

    def get(self, request, *args, **kwargs):
        artists = Artists.objects.all().order_by(
            "start_date"
        )  # Get all artists adn order by start date
        artists_to_send = []  # Empty array to append artists to send to template
        for artist in artists:  # Do this for each artist
            valid_bookings_count = 0  # Set bookings counter
            rating_total = 0  # Set rating score total
            valid_bookings = Bookings.objects.filter(is_rated=True).filter(
                booked_artist=artist.id
            )  # Filter only bookings that are rated
            for (
                valid_booking
            ) in valid_bookings:  # For each booking that is rated perform this
                valid_bookings_count = (
                    valid_bookings_count + 1
                )  # Increase rated bookings counter
                rating_total = (
                    rating_total + valid_booking.rating
                )  # Add score of the current booking
                rating = rating_total / valid_bookings_count  # Count average rating
            if valid_bookings_count == 0:  # If no rated bookings for artist
                rating = 0  # Set rating to 0 (if else statement in template)
            artists_to_send.append(  # Append to array to send to template
                {
                    "artist": artist,  # Details of artist
                    "rating": rating,  # Average rating
                    "rating_count": valid_bookings_count,  # Rated bookings
                }
            )
        return render(  # Render template and send "artist_list"
            request,
            self.template_name,
            {
                "artists_list": artists_to_send,
            },
        )


class TeamDetailView(generic.DetailView):
    """
    Class renders details of single artist for template
    """

    template_name = "artists/artist_detail.html"  # Template
    model = Artists  # Model to be used
    slug_field = "slug"  # Name of slug field

    def get(self, request, *args, **kwargs):
        artist_selected = self.get_object()  # Select artist by slug
        styles_this_artist = StylesAvailable.objects.filter(
            artists__in=[artist_selected]
        )  # Filter styles for selected artist
        style_slug = styles_this_artist.values_list(
            "slug", flat=True
        )  # Set a slug field for all styles with current artist
        filtered_styles = zip(
            style_slug, styles_this_artist
        )  # Zip name of style and slug into this variable
        valid_bookings_count = 0  # Set bookings counter
        rating_total = 0  # Set score rating counter
        valid_bookings = Bookings.objects.filter(is_rated=True).filter(
            booked_artist=artist_selected.id
        )  # Filter all rated bookings for current artist
        for valid_booking in valid_bookings:  # For each rated booking do this
            valid_bookings_count = (
                valid_bookings_count + 1
            )  # Increase counter of rated bookings
            rating_total = (
                rating_total + valid_booking.rating
            )  # Add score of the current booking
            rating = rating_total / valid_bookings_count  # Count average rating
        if valid_bookings_count == 0:  # If no rated bookings for artist
            rating = 0  # Set rating to 0 (if else statement in template)
        return render(  # Render template with following
            request,
            self.template_name,
            {
                "artist_selected": artist_selected,  # Artist
                "filtered_styles": filtered_styles,  # Artist's styles
                "rating": rating,  # Artist's rating
                "bookings_total": valid_bookings_count,  # Rated bookings
            },
        )
