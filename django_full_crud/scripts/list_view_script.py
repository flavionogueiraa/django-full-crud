def list_view_script(app_name, model_name, snake_model_name):
    return f"""from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ...models import {model_name}


class {model_name}ListView(LoginRequiredMixin, ListView):
    model = {model_name}

    template_name = "{app_name}/{snake_model_name}/{snake_model_name}_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
"""
