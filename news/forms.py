# Imports
from news.models import NewsComments
from django import forms


class NewsCommentForm(forms.ModelForm):
    """Form for comments"""

    class Meta:
        model = NewsComments
        fields = ("comment_body",)
