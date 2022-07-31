from os.path import basename


def replaced_module(module):
    return basename(module.replace(".py", ""))
