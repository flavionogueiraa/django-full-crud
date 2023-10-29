# flake8: noqa
from django_full_crud.globals import get_django_full_crud_json


def serializer_script(model_name):
    serializer_imports = get_django_full_crud_json("serializer_imports", "")
    replaced_serializer_imports = [
        serializer_import.replace("'", "") + "\n"
        for serializer_import in serializer_imports
    ]
    return f"""from rest_framework import serializers
{"".join(replaced_serializer_imports)}
from ..models import {model_name}


class {model_name}Serializer({get_django_full_crud_json("serializer_superclass", "serializers.ModelSerializer")}):
    class Meta:
        model = {model_name}
        fields = "__all__"
"""
