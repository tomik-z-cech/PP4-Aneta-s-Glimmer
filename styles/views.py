from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.db.models import Count, Q
from styles.models import StylesAvailable, StylesComments
from artists.models import Artists
from styles.forms import StylesCommentForm


# ----------------------- STYLES VIEWS --------------------- #


class StylesView(generic.ListView):
    template_name = "styles/styles.html"

    def get(self, request, *args, **kwargs):
        # Select all news
        styles_list = StylesAvailable.objects.annotate(
            comments_num=Count("style_comments", filter=Q(style_comments__approved=1))
        ).all()
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
        comments = (
            StylesComments.objects.filter(style__in=[style_selected])
            .filter(approved=1)
            .order_by("-created_on")
        )
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
                "style": style_selected,
                "filtered_artists": filtered_artists,
                "liked": liked,
                "want_to_try": want_to_try,
                "users_liked": users_liked_styles,
                "users_want_to_try": users_want_to_try_styles,
                "styles_comment_form": StylesCommentForm(),
                "comments": comments,
                "can_comment": True,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Function is called when comment submitted
        """
        style_selected = self.get_object()
        artists_with_style = Artists.objects.filter(styles__in=[style_selected])
        artists_slug = artists_with_style.values_list("slug", flat=True)
        filtered_artists = zip(artists_slug, artists_with_style)
        users_liked_styles = style_selected.likes.all()
        users_want_to_try_styles = style_selected.want_to_try.all()
        comments = StylesComments.objects.filter(style__in=[style_selected]).filter(
            approved=1
        )
        liked = False
        if style_selected.likes.filter(id=self.request.user.id).exists():
            liked = True
        want_to_try = False
        if style_selected.want_to_try.filter(id=self.request.user.id).exists():
            want_to_try = True
        styles_comment_form = StylesCommentForm(data=request.POST)
        # If form valid save comment
        if styles_comment_form.is_valid():
            styles_comment_form.instance.creator = request.user
            style_comment = styles_comment_form.save(commit=False)
            style_comment.style = style_selected
            style_comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Your comment on {style_selected.style_name} is awaiting approval ;)",
            )
        # If not valid, return form
        else:
            styles_comment_form = StylesCommentForm()
        return render(  # Render template
            request,
            self.template_name,
            {
                "style": style_selected,
                "filtered_artists": filtered_artists,
                "liked": liked,
                "want_to_try": want_to_try,
                "users_liked": users_liked_styles,
                "users_want_to_try": users_want_to_try_styles,
                "styles_comment_form": StylesCommentForm(),
                "comments": comments,
                "can_comment": False,
            },
        )


class StyleLike(LoginRequiredMixin, View):
    def post(self, request, slug):
        style = get_object_or_404(StylesAvailable, slug=slug)

        if style.likes.filter(id=request.user.id).exists():
            style.likes.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS, f"You disliked {style.style_name} :( "
            )
        else:
            style.likes.add(request.user)
            messages.add_message(
                request, messages.SUCCESS, f"You liked {style.style_name} ;)"
            )

        return HttpResponseRedirect(reverse("style-detail", args=[slug]))


class StyleTry(LoginRequiredMixin, View):
    def post(self, request, slug):
        style = get_object_or_404(StylesAvailable, slug=slug)

        if style.want_to_try.filter(id=request.user.id).exists():
            style.want_to_try.remove(request.user)
            messages.add_message(
                request,
                messages.SUCCESS,
                f"You unmarked {style.style_name} as style to try :( ",
            )
        else:
            style.want_to_try.add(request.user)
            messages.add_message(
                request,
                messages.SUCCESS,
                f"You marked {style.style_name} as style to try :( ",
            )

        return HttpResponseRedirect(reverse("style-detail", args=[slug]))
