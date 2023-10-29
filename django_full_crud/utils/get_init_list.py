import inspect
from importlib import import_module

from django_full_crud.globals import BAR, get_project_dir
from django_full_crud.utils.get_modules import get_modules
from django_full_crud.utils.replaced_module import replaced_module


def format_parameter(parameter):
    return parameter.__str__().replace(" ", "").split(":")


def get_init_list(app_name, folder):
    dict_param = {}
    if not BAR in folder:
        all_modules = getattr(import_module(f"{app_name}.{folder}"), "__all__")
        only_has_name = list(
            filter(lambda module: hasattr(module, "__name__"), all_modules)
        )
        for module in only_has_name:
            module_name = module.__name__
            inspect_module = inspect.signature(module)
            parameters = list(inspect_module.parameters.values())

            for parameter in parameters:
                formated_parameter = format_parameter(parameter)
                if len(formated_parameter) > 1:
                    dict_param[module_name] = {
                        formated_parameter[0]: formated_parameter[1]
                    }

    directory = get_project_dir(f"{app_name}{BAR}{folder}")
    modules = get_modules(directory)

    init_list = [
        make_init_object(module, dict_param)
        for module in modules
        if is_a_valid_module(module["module"])
    ]

    return init_list


def is_a_valid_module(module):
    return not module.endswith("__init__.py")


def only_necessary_module(module):
    is_init = module["module"].endswith("__init__.py")
    is_py_cache = module["module"].endswith("__pycache__")
    return not is_init and not is_py_cache


def make_init_object(module, dict_param):
    module_name = replaced_module(module["module"])
    return {
        "archive_name": module_name,
        "class_function_name": get_class_function_name(module),
        "parameters": dict_param.get(module_name, {}),
        "folder": module["folder"],
        "childrens": [
            make_init_object(children, dict_param)
            for children in module["childrens"]
        ],
    }


def check_admin_path_exists(app_name, init):
    import os

    from globals.main import get_project_dir

    admin_file_path = f"{app_name}{BAR}admin{BAR}{init['archive_name']}.py"
    path_exists = os.path.exists(get_project_dir(admin_file_path))

    return path_exists


def check_form_path_exists(app_name, init):
    import os

    from globals.main import get_project_dir

    form_file_path = f"{app_name}{BAR}forms{BAR}{init['archive_name']}.py"
    path_exists = os.path.exists(get_project_dir(form_file_path))

    return path_exists


def check_views_path_exists(app_name, init):
    import os

    from globals.main import get_project_dir

    file_path = f"{app_name}{BAR}views{BAR}{init['archive_name']}.py"
    path_exists = os.path.exists(get_project_dir(file_path))

    return path_exists


def get_class_function_name(module):
    if module["folder"]:
        return replaced_module(module["module"])

    path = module["module"]
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        def_or_class = list(filter(starts_with_class_or_def, lines))
        right_line = def_or_class[0] if def_or_class else ""
        class_function_name = make_splits_line(right_line)
        return class_function_name


def starts_with_class_or_def(string):
    return string.startswith("class ") or string.startswith("def ")


def make_splits_line(line):
    class_or_def_part = line.split("(")[0]
    if class_or_def_part:
        only_name_part = class_or_def_part.split()[-1]
        return only_name_part
    return ""
