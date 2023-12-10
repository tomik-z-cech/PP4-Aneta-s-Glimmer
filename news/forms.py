from news.models import NewsComments
from django import forms


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComments
        fields = ('comment_body',)