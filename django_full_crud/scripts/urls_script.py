import django_full_crud.utils as utils

from .init_script import get_only_files, get_only_folders


def urls_script(app_name, init_list, viewset_init_list):
    view_only_files = get_only_files(init_list)
    view_only_folders = get_only_folders(init_list)
    viewset_only_files = get_only_files(viewset_init_list)

    script = write_imports_and_app_router(app_name)
    script = write_routers(script, app_name, viewset_only_files)
    script = write_folder_pattenrs(script, view_only_folders)
    script += f"""urlpatterns = (\n\t[
        path("api/", include({app_name}_router.urls)),"""

    script = write_files_path(script, view_only_files)
    script += "\n\t]"

    script = write_sum_folders_patterns(script, view_only_folders)
    script += "\n)\n"

    return script


def write_imports_and_app_router(app_name):
    return f"""from django.urls import include, path
from rest_framework import routers

from {app_name} import views, viewsets

{app_name}_router = routers.DefaultRouter()
"""


def write_sum_folders_patterns(script, view_only_folders):
    for folder in view_only_folders:
        script += f"\n\t+ {folder['class_function_name']}_patterns"
    return script


def write_files_path(script, view_only_files):
    for file in view_only_files:
        name = file["class_function_name"]
        kebab_case = to_kebab_case(name)
        snake_case = utils.camel_to_snake_case(name)
        script += f"""\n\t\tpath("{kebab_case}/{param_or_not(file)}", views.{name}{as_view_or_not(name)}, name="{snake_case}"),"""
    return script


def write_routers(script, app_name, viewset_only_files):
    router_name = f"{app_name}_router"
    print(viewset_only_files)
    for file in viewset_only_files:
        name = file["class_function_name"]
        name_without_suffix = name.replace("ViewSet", "")
        kebab_case = to_kebab_case(name_without_suffix)
        snake_case = utils.camel_to_snake_case(name_without_suffix)
        script += f"""{router_name}.register("{kebab_case}", viewsets.{name}, basename="{snake_case}")\n\n"""
    return script


def write_folder_pattenrs(script, view_only_folders):
    for folder in view_only_folders:
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
