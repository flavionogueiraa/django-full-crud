def form_script(model_name):
    return f"""from django import forms

from ..models import {model_name}


class {model_name}Form(forms.ModelForm):
    class Meta:
        model = {model_name}

        fields = "__all__"
"""
