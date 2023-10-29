# flake8: noqa
def form_template_script(class_info):
    fields = list(map(make_field, class_info["form_fields"]))

    return """{% extends 'base.html' %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        <div>{{form.errors}}</div>
        """ + default_join(fields) + """
        <a href="javascript:window.history.back();">Cancelar</a>
        <button type="submit">Salvar</button>
    </form>
{% endblock %}
"""


def make_field(field):
    return "<label for='{{form." + field + ".id_for_label}}'>{{form." + field + ".label}}</label>\n        {{form." + field + "}}"


def default_join(list):
    return "\n        ".join(list)
