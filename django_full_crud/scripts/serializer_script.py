from importlib import import_module

from django_full_crud.utils import get_prop


def serializer_script(app_name, snake_model_name, model_name):
    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")

    foreign_keys = get_prop(class_object, "foreign_keys", str=False)
    related_apps = []
    related_models = []
    # print(dir(getattr(class_object, foreign_keys[0]).field))

    for foreign_key in foreign_keys:
        app = getattr(
            class_object, foreign_key
        ).field.related_model._meta.app_label
        related_apps.append(app)

        model = getattr(class_object, foreign_key).field.related_model.__name__
        related_models.append(model)

    properties = list(class_object._meta._property_names)
    properties.remove("pk")

    if properties:
        only_custom_properties = [
            f"{property} = serializers.ReadOnlyField()"
            for property in properties
        ]
    else:
        only_custom_properties = []

    list_foreign_keys = [
        f"{foreign_key} = serializers.ReadOnlyField()"
        for foreign_key in foreign_keys
    ]

    return f"""from rest_framework import serializers

from {app_name}.models import {model_name}
{write_imports(related_apps, related_models)}


class {model_name}Serializer(serializers.ModelSerializer):
	{default_join(only_custom_properties)}
	class Meta:
		model = {model_name}
		fields = "__all__"
"""


def default_join(list):
    return "\n\n\t".join(list) + "\n" if list else ""


def write_imports(related_apps, related_models):
    imports = []
    for app, model in zip(related_apps, related_models):
        imports.append(f"from {app}.serializers import {model}Serializer")

    return "\n".join(imports)
