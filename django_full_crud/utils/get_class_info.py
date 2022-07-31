from functools import partial
from importlib import import_module


def get_class_info(app_name, model_name):
    module = import_module(f"{app_name}.models")
    class_name = getattr(module, model_name)

    get_verbose_name = partial(get_attr_field, "verbose_name")
    get_name = partial(get_attr_field, "name")

    fields = class_name._meta.get_fields()

    fields_verbose_name = list(map(get_verbose_name, fields))
    fields_name = list(map(get_name, fields))
    form_fields = fields_name[1:]

    return {
        "class_verbose_name": class_name._meta.verbose_name,
        "class_verbose_name_plural": class_name._meta.verbose_name_plural,
        "fields_name": fields_name,
        "fields_verbose_name": fields_verbose_name,
        "form_fields": form_fields,
    }


def get_attr_field(attr, field):
    if hasattr(field, attr):
        return getattr(field, attr)
    else:
        return "-"

def only_original(field):
    return not hasattr(field, "field")
