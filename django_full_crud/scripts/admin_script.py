# flake8: noqa
from importlib import import_module

from django_full_crud.globals import get_django_full_crud_json
from django_full_crud.utils import get_prop


def admin_script(app_name, snake_model_name, model_name):
    simple_admin = get_django_full_crud_json("simple_admin", False)
    admin_imports = get_django_full_crud_json("admin_imports", "")
    replaced_admin_imports = [
        admin_import.replace("'", "") + "\n" for admin_import in admin_imports
    ]
    if simple_admin:
        return f"""from django.contrib import admin
{default_join(replaced_admin_imports)}
from ..models import {model_name}


@admin.register({model_name})
class {model_name}Admin({get_django_full_crud_json("admin_superclass", "admin.ModelAdmin")}):
    ...
"""

    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")

    list_display = get_prop(class_object, "list_display")
    search_fields = get_prop(class_object, "search_fields")
    list_filter = get_prop(class_object, "list_filter")
    autocomplete_fields = get_prop(class_object, "autocomplete_fields")
    filter_horizontal = get_prop(class_object, "filter_horizontal")

    script = f"""from django.contrib import admin

from ..models import {model_name}


@admin.register({model_name})
class {model_name}Admin({get_django_full_crud_json("admin_superclass", "admin.ModelAdmin")}):
    list_display = [
        {default_join(list_display)}
    ]

    search_fields = [
        {default_join(search_fields)}
    ]
"""

    if list_filter:
        script += f"""
    list_filter = [
        {default_join(list_filter)}
    ]
"""

    if autocomplete_fields:
        script += f"""
    autocomplete_fields = [
        {default_join(autocomplete_fields)}
    ]
"""

    if filter_horizontal:
        script += f"""
    filter_horizontal = [
        {default_join(filter_horizontal)}
    ]
"""

    return script


def default_join(list):
    return "\n        ".join(list)
