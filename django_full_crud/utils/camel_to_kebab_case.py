import re


def camel_to_kebab_case(string):
    string = re.sub(r"(?<!^)(?=[A-Z])", "-", string).lower()
    return string
