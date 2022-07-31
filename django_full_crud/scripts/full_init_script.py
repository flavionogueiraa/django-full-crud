from django_full_crud.utils import get_init_list


def full_init_script(app_name, folder_name):
    init_list = get_init_list(app_name, folder_name)
    script = ""
    for init in init_list:
        script += make_import_line(init)
    
    for init in init_list:
        script += make_views_line(init)

    script += "\n__all__ = (\n\t[]\n"
    for init in init_list:
        script += make_all_line(init)
    script += ")\n"

    return script


def make_import_line(init_object):
    archive_name = init_object["archive_name"]
    class_name = init_object["class_name"]
    return f"""from .{archive_name} import (
    {class_name}CreateView,
    {class_name}DeleteView,
    {class_name}DetailView,
    {class_name}ListView,
    {class_name}UpdateView,
)
"""

def make_views_line(init_object):
    archive_name = init_object["archive_name"]
    class_name = init_object["class_name"]
    return f"""\n{archive_name}_views = [
    {class_name}CreateView,
    {class_name}DeleteView,
    {class_name}DetailView,
    {class_name}ListView,
    {class_name}UpdateView,
]
"""


def make_all_line(init_object):
    archive_name = init_object["archive_name"]
    return f"\t+ {archive_name}_views\n"
