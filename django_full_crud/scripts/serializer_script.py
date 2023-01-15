from importlib import import_module


def serializer_script(app_name, snake_model_name, model_name):
    module = import_module(f"{app_name}.models.{snake_model_name}")
    class_object = getattr(module, f"{model_name}")
    properties = list(class_object._meta._property_names)
    properties.remove("pk")

    if properties:
        only_custom_properties = [
            f"{property} = serializers.ReadOnlyField()"
            for property in properties
        ]
    else:
        only_custom_properties = []

    return f"""from rest_framework import serializers

from ..models import {model_name}


class {model_name}Serializer(serializers.ModelSerializer):
	{default_join(only_custom_properties)}
	class Meta:
		model = {model_name}
		fields = "__all__"
"""


def default_join(list):
    return "\n\n\t".join(list) + "\n" if list else ""
