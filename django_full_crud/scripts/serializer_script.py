from importlib import import_module

from django_full_crud.utils import get_prop


def serializer_script(app_name, snake_model_name, model_name):
    script = write_default_imports(app_name, model_name)

    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")

    foreign_keys = get_prop(class_object, "foreign_keys", str=False)
    serializers_import = []
    foreign_keys_serializers = []

    for foreign_key in foreign_keys:
        app = getattr(
            class_object,
            foreign_key,
        ).field.related_model._meta.app_label

        model = getattr(
            class_object,
            foreign_key,
        ).field.related_model.__name__

        serializers_import.append(
            f"from {app}.serializers import {model}Serializer\n"
        )

        foreign_keys_serializers.append(
            f"""default_return["{foreign_key}"] = {model}Serializer(
            instance.{foreign_key}
        ).data"""
        )

    if serializers_import:
        script += "".join(serializers_import)

    script += (
        f"\n\nclass {model_name}Serializer(serializers.ModelSerializer):\n    "
    )

    properties = list(class_object._meta._property_names)
    properties.remove("pk")

    if properties:
        only_custom_properties = [
            f"{property} = serializers.ReadOnlyField()"
            for property in properties
        ]
    else:
        only_custom_properties = []

    if only_custom_properties:
        script += default_join(only_custom_properties)
        script += "\n    "

    if foreign_keys_serializers:
        script += f"""def to_representation(self, instance):
        default_return = super(
            {model_name}Serializer,
            self,
        ).to_representation(instance)

        {second_join(foreign_keys_serializers)}
        return default_return\n\n    """

    script += f"""class Meta:
        model = {model_name}
        fields = "__all__"
"""

    return script


def default_join(list):
    return "\n\n    ".join(list) + "\n" if list else ""


def second_join(list):
    return "\n\n        ".join(list) + "\n" if list else ""


def write_default_imports(app_name, model_name):
    return f"""from rest_framework import serializers

from {app_name}.models import {model_name}\n"""
