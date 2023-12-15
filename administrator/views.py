from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class AllAdminView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    template_name = "administrator/admin_styles.html"  # Template

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        return render(  # Render template
            request,
            self.template_name,
            {"news_detail": "1"},
        )
