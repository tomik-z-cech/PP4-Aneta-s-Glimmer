# Imports
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from news.models import NewsPosts, NewsComments
from news.forms import NewsCommentForm


class AllNewsView(generic.ListView):
    """
    View generates view of all news posts
    """

    template_name = "news/all_news.html"  # Template

    def get(self, request, *args, **kwargs):
        """Method generates view of all news"""
        # Select all news
        news = NewsPosts.objects.annotate(
            comments_num=Count(
                "news_comments", filter=Q(news_comments__approved=1)
            )
        ).filter(is_published=1)
        # Render template and send news
        return render(
            request,
            self.template_name,
            {
                "news_list": news,
            },
        )


class NewsDetailView(generic.DetailView):
    """
    View generates view of selected post
    """

    template_name = "news/news_detail.html"  # Template

    def get(self, request, slug, *args, **kwargs):
        """
        Function is called when page accessed
        """
        search_query = NewsPosts.objects.filter(
            is_published=1
        )  # Select all posts that are published
        post = get_object_or_404(
            search_query, slug=slug
        )  # Select the current news post
        # Select all comments approved for current post
        comments = (
            NewsComments.objects.filter(approved=True)
            .filter(post__in=[post])
            .order_by("created_on")
        )
        # Get a list of all users that liked the post
        users_liked = post.likes.all()
        liked = False  # Set variable for current user
        # If current user in people, set liked to true
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(  # Render template
            request,
            self.template_name,
            {
                "news_detail": post,
                "comments": comments,
                "liked": liked,
                "news_comment_form": NewsCommentForm(),
                "users_liked": users_liked,
                "can_comment": True,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Function is called when comment submitted
        """
        post = get_object_or_404(NewsPosts, slug=slug)  # Get current news post
        comments = (
            NewsComments.objects.filter(approved=True)
            .filter(post__in=[post])
            .order_by("created_on")
        )
        liked = False  # Pre-set variable like
        users_liked = post.likes.all()
        # If current user likes
        if post.likes.filter(id=self.request.user.id).exists():
            # Set like to True
            liked = True
        # Get comment from form
        news_comment_form = NewsCommentForm(data=request.POST)
        # If form valid save comment
        if news_comment_form.is_valid():
            news_comment_form.instance.username = request.user
            new_comment = news_comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Your comment on post {new_comment.post} pending approval.",
            )  # User message
        # If not valid, return form
        else:
            news_comment_form = NewsCommentForm()
        return render(  # Render template
            request,
            self.template_name,
            {
                "news_detail": post,
                "comments": comments,
                "liked": liked,
                "news_comment_form": NewsCommentForm(),
                "users_liked": users_liked,
                "can_comment": False,
            },
        )


class NewsPostLike(LoginRequiredMixin, View):
    """
    View sets likes on News Posts
    """

    def post(self, request, slug):
        """
        Function called when like button clicked
        """
        # select current News Post
        post = get_object_or_404(NewsPosts, slug=slug)
        # If the user already liked the post, remove like
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS, f"You disliked {post.title} :( "
            )
        # If not liked, add like
        else:
            post.likes.add(request.user)
            messages.add_message(
                request, messages.SUCCESS, f"You liked {post.title} ;) "
            )
        # Reverse back to news-detail
        return HttpResponseRedirect(reverse("news-detail", args=[slug]))
