def create_view_script(app_name, model_name, snake_model_name):
    return f"""from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from ...forms import {model_name}Form
from ...models import {model_name}


class {model_name}CreateView(LoginRequiredMixin, CreateView):
    model = {model_name}

    form_class = {model_name}Form

    template_name = "{app_name}/{snake_model_name}/{snake_model_name}_form.html"

    def get_success_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy("{snake_model_name}_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
"""
