from django_full_crud.utils import get_init_list


def init_script(app_name, folder):
    init_list = get_init_list(app_name, folder)
    only_files = get_only_files(init_list)
    only_folders = get_only_folders(init_list)

    script = ""
    script = write_imports(script, init_list)
    if only_folders:
        script = write_views_lists(script, only_folders)
        script = write_all_folders_list(script, only_files, only_folders)
    else:
        script = write_all_files_list(script, only_files)
    return script

def get_only_files(init_list):
    return list(filter(lambda init: not init["folder"], init_list))

def get_only_folders(init_list):
    return list(filter(lambda init: init["folder"], init_list))

def write_imports(script, init_list):
    for init in init_list:
        make_import_line = (
            make_full_import_line if init["folder"] else make_simple_import_line
        )
        script += make_import_line(init)
    
    script += "\n"
    return script

def write_views_lists(script, only_folders):
    for init in only_folders:
        script += make_views_line(init)
    
    return script

def write_all_folders_list(script, only_files, only_folders):
    script += "\n__all__ = (\n\t[\n"

    for init in only_files:
        script += make_all_line(init, "\t\t")
    script += "\t]"

    for init in only_folders:
        script += make_folder_line(init)

    script += "\n)\n"

    return script

def write_all_files_list(script, only_files):
    script += "__all__ = [\n"

    for init in only_files:
        script += make_all_line(init, "\t")
    script += "]\n"

    return script


def make_simple_import_line(init_object):
    archive_name = init_object["archive_name"]
    class_function_name = init_object["class_function_name"]
    return f"from .{archive_name} import {class_function_name}\n"


def make_full_import_line(init_object):
    archive_name = init_object["archive_name"]
    childrens = [children.get("class_function_name") for children in init_object["childrens"]]

    return (
        f"""from .{archive_name} import (
    """
        + default_join(childrens)
        + """,
)\n"""
    )


def make_all_line(init_object, tabs):
    class_function_name = init_object["class_function_name"]
    return f"{tabs}{class_function_name},\n"


def make_folder_line(init_object):
    return f"\n\t+ {init_object['archive_name']}_views"


def default_join(list):
    return ",\n\t".join(list)


def make_views_line(init_object):
    archive_name = init_object["archive_name"]
    childrens = [children.get("class_function_name") for children in init_object["childrens"]]

    return (
        f"""{archive_name}_views = [
    """
        + default_join(childrens)
        + """,
]\n"""
    )
