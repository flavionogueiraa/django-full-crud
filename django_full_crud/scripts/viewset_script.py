# flake8: noqa
from importlib import import_module

from django_full_crud.globals import get_django_full_crud_json
from django_full_crud.utils import get_prop


def viewset_script(app_name, model_name, snake_model_name):
    simple_viewset = get_django_full_crud_json("simple_viewset", False)
    viewset_imports = get_django_full_crud_json("viewset_imports", "")
    replaced_viewset_imports = [
        viewset_import.replace("'", "") + "\n"
        for viewset_import in viewset_imports
    ]
    if simple_viewset:
        return f"""from rest_framework import viewsets
{default_join(replaced_viewset_imports)}

from ..models import {model_name}
from {app_name}.serializers import {model_name}Serializer


class {model_name}ViewSet({get_django_full_crud_json("viewset_superclass", "viewsets.ModelViewSet")}):
    queryset = {model_name}.objects.all()

    serializer_class = {model_name}Serializer
"""
    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")

    search_fields = get_prop(class_object, "search_fields")
    filterset_fields = get_prop(class_object, "filterset_fields")
    ordering_fields = get_prop(class_object, "ordering_fields")

    return f"""from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import {model_name}
from {app_name}.serializers import {model_name}Serializer


class {model_name}ViewSet({get_django_full_crud_json("viewset_superclass", "viewsets.ModelViewSet")}):
    queryset = {model_name}.objects.all()

    serializer_class = {model_name}Serializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    search_fields = [
        {default_join(search_fields)}
    ]

    filterset_fields = [
        {default_join(filterset_fields)}
    ]

    ordering_fields = [
        {default_join(ordering_fields)}
    ]
"""


def default_join(list):
    return "\n        ".join(list)
