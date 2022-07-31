import django_full_crud.utils as utils

from .init_script import get_only_files, get_only_folders


def urls_script(app_name, init_list):
    only_files = get_only_files(init_list)
    only_folders = get_only_folders(init_list)

    script = write_imports(app_name)
    script = write_folder_pattenrs(script, only_folders)
    script += f"urlpatterns = (\n\t["

    script = write_files_path(script, only_files)
    script += "\n\t]"

    script = write_sum_folders_patterns(script, only_folders)
    script += "\n)\n"

    return script


def write_imports(app_name):
    return f"""from django.urls import path

from {app_name} import views

"""


def write_sum_folders_patterns(script, only_folders):
    for folder in only_folders:
        script += f"\n\t+ {folder['class_function_name']}_patterns"
    return script


def write_files_path(script, only_files):
    for file in only_files:
        name = file["class_function_name"]
        kebab_case = to_kebab_case(name)
        snake_case = utils.camel_to_snake_case(name)
        script += f"""\n\t\tpath("{kebab_case}/{param_or_not(file)}", views.{name}{as_view_or_not(name)}, name="{snake_case}"),"""
    return script


def write_folder_pattenrs(script, only_folders):
    for folder in only_folders:
        script += f"{folder['class_function_name']}_patterns = ["
        for children in folder["childrens"]:
            children_name = children.get("class_function_name")

            kebab_case = to_kebab_case(children_name)
            snake_case = utils.camel_to_snake_case(children_name)
            script += f"""\n\tpath("{kebab_case}/{param_or_not(children)}", views.{children_name}{as_view_or_not(children_name)}, name="{snake_case}"),"""
        script += "\n]\n\n"
    return script


def to_kebab_case(string):
    if "_" in string:
        return utils.snake_to_kebab_case(string)
    return utils.camel_to_kebab_case(string)


def as_view_or_not(string):
    if string[0].isupper():
        return ".as_view()"
    return ""


def param_or_not(children):
    children_name = children.get("class_function_name")
    is_delete_view = "Delete" in children_name
    is_detail_view = "Detail" in children_name
    is_update_view = "Update" in children_name
    if is_delete_view or is_detail_view or is_update_view:
        return "<int:pk>/"

    url_parameters = ""

    parameters = children.get("parameters", {})
    for key in parameters:
        url_parameters += f"<{parameters[key]}:{key}>/"
    return url_parameters
