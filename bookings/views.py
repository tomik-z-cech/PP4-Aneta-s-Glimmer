from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "base.html",
        )

