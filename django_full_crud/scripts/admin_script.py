from importlib import import_module

props_dict = {
    "list_display": [
        "BigAutoField",
        "BooleanField",
        "CharField",
        "DateField",
        "DateTimeField",
        "DecimalField",
        "ForeignKey",
        "IntegerField",
        "PositiveIntegerField",
    ],
    "search_fields": [
        "BigAutoField",
        "CharField",
        "DateField",
        "DateTimeField",
        "DecimalField",
        "IntegerField",
        "PositiveIntegerField",
    ],
    "list_filter": [
        "BooleanField",
        "DateField",
        "DateTimeField",
        "ForeignKey",
    ],
    "autocomplete_fields": [
        "ForeignKey",
    ],
    "filter_horizontal": [
        "ManyToManyField",
    ],
}


def get_prop(model, prop):
    props = []
    fields = model._meta.get_fields()
    for field in fields:
        field_type = field.get_internal_type()
        is_original_field = not hasattr(field, "field")

        if field_type in props_dict[prop] and is_original_field:
            field_str = f'"{field.name}",'
            props.append(field_str)

    return props


def admin_script(app_name, snake_model_name, model_name):
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
class {model_name}Admin(admin.ModelAdmin):
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
    return "\n\t\t".join(list)
