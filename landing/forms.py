from django import forms

class SearchBarForm(forms.Form):
    search_query = forms.CharField(max_length=255)