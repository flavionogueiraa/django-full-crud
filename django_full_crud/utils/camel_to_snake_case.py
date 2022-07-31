import re


def camel_to_snake_case(string):
    string = re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()
    return string
