def form_template_script(class_info):
    fields = list(map(make_field, class_info["form_fields"]))

    return """{% extends 'base.html' %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        """ + default_join(fields) + """
        <a href="javascript:window.history.back();">Cancelar</a>
        <button type="submit">Salvar</button>
    </form>
{% endblock %}
"""


def make_field(field):
    return "{{form." + field + "}}"


def default_join(list):
    return "\n\t\t".join(list)
