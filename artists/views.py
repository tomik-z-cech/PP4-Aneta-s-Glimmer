from django.shortcuts import render
from django.views import generic
from bookings.models import StylesAvailable, Artists


# ----------------------- TEAM VIEWS --------------------- # 

class TeamView(generic.ListView):
    model = Artists
    queryset = Artists.objects.all()
    template_name = 'artists/artists.html'
    context_object_name = 'artists_list'

class TeamDetailView(generic.DetailView):
    template_name = 'artists/artist_detail.html'
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
