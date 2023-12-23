# PEP8
# Imports
from news.models import NewsComments
from django import forms


class NewsCommentForm(forms.ModelForm):
    """Form for comments"""

    class Meta:
        model = NewsComments
        fields = ("comment_body",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_body'].widget.attrs.update({
            'rows': 3,
            'placeholder': 'Type your comment here ...',
        })
