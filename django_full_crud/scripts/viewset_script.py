from importlib import import_module

from django_full_crud.utils import get_prop


def viewset_script(app_name, model_name, snake_model_name):
    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")

    search_fields = get_prop(class_object, "search_fields")
    filterset_fields = get_prop(class_object, "filterset_fields")

    return f"""from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import {model_name}
from {app_name}.serializers import {model_name}Serializer


class {model_name}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name}.objects.all()

    serializer_class = {model_name}Serializer

    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        {default_join(search_fields)}
    ]

    filterset_fields = [
        {default_join(filterset_fields)}
    ]

    ordering_fields = [
    ]

    search_fields = [
    ]
"""


def default_join(list):
    return "\n        ".join(list)
