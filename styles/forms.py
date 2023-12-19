# Imports
from styles.models import StylesComments
from django import forms


class StylesCommentForm(forms.ModelForm):
    """Form for comments"""

    class Meta:
        model = StylesComments
        fields = ("comment_body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_body'].widget.attrs['rows'] = 3