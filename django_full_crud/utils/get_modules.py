import glob
from os.path import join

from .replaced_module import replaced_module


def only_necessary_module(module):
    is_init = module["module"].endswith("__init__.py")
    is_py_cache = module["module"].endswith("__pycache__")
    return not is_init and not is_py_cache

def get_modules(directory):
    modules = list(
        map(
            lambda module: {"module": module, "module_name": replaced_module(module), "folder": False, "childrens": []},
            glob.glob(join(directory, "*")),
        )
    )

    modules = list(filter(only_necessary_module, modules))

    for module in modules:
        module["childrens"] = get_modules(module["module"])
        if module["childrens"]:
            module["folder"] = True

    return modules
