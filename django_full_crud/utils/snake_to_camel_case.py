def snake_to_camel_case(snake_str):
    components = snake_str.split("_")
    # Sim, foi copiado daqui: https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return "".join(x.title() for x in components)
