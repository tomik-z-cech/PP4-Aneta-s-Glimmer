# PEP8
# Imports
from django import forms


class SearchBarForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=True)

    class Meta:
        fields = ("search_query",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search_query"].widget.attrs.update(
            {
                "placeholder": "What are you looking for ?",
            }
        )
