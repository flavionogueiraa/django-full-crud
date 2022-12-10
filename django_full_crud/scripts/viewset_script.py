def viewset_script(app_name, model_name):
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
        
    ]
"""
