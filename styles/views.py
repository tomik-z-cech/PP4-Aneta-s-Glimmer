from django.shortcuts import render
from django.views import generic
from bookings.models import StylesAvailable, Artists


# ----------------------- STYLES VIEWS --------------------- #


class StylesView(generic.ListView):
    model = StylesAvailable
    queryset = StylesAvailable.objects.all()
    template_name = "styles/styles.html"
    context_object_name = "styles_list"


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
        return render(
            request,
            self.template_name,
            {
                "style_name": style_selected.style_name,
                "style_description": style_selected.style_description,
                "sample_image": style_selected.sample_image,
                "likes": style_selected.number_of_likes,
                "tries": style_selected.number_of_tries,
                "filtered_artists": filtered_artists,
            },
        )
