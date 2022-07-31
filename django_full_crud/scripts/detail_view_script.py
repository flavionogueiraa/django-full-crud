def detail_view_script(app_name, model_name, snake_model_name):
    return f"""from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from ...models import {model_name}


class {model_name}DetailView(LoginRequiredMixin, DetailView):
    model = {model_name}

    template_name = "{app_name}/{snake_model_name}/{snake_model_name}_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
"""
