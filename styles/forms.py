# Imports
from styles.models import StylesComments
from django import forms


class StylesCommentForm(forms.ModelForm):
    """Form for comments"""

    class Meta:
        model = StylesComments
        fields = ("comment_body",)