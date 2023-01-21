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
    "foreign_keys": [
        "ForeignKey",
    ],
}


def get_prop(model, prop, str=True):
    props = []
    fields = model._meta.get_fields()
    for field in fields:
        field_type = field.get_internal_type()
        is_original_field = not hasattr(field, "field")

        if field_type in props_dict[prop] and is_original_field:
            if str:
                field_str = f'"{field.name}",'
                props.append(field_str)
            else:
                props.append(field.name)

    return props
