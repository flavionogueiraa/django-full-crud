def serializer_script(model_name):
    return f"""from rest_framework import serializers

from ..models import {model_name}


class {model_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = "__all__"

"""
