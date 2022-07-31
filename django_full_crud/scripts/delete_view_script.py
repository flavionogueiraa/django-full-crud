def delete_view_script(app_name, model_name, snake_model_name):
    return f"""from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from ...models import {model_name}


class {model_name}DeleteView(LoginRequiredMixin, DeleteView):
    model = {model_name}

    template_name = "{app_name}/{snake_model_name}/{snake_model_name}_delete.html"

    def get_success_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy("{snake_model_name}_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
"""
