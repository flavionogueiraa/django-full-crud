def list_template_script(class_info):
    ths = list(map(make_th, class_info["fields_verbose_name"]))
    tds = list(map(make_td, class_info["fields_name"]))

    return (
        """{% extends 'base.html' %}

{% block content %}
    <div>
        <h1>Listagem de """ + class_info["class_verbose_name_plural"] + """</h1>
        <table>
            <thead>
                <tr>
                    """ + default_join(ths) + """
                </tr>
            </thead>
            <tbody>
                {% for object in object_list %}
                    """ + default_join(tds) + """
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
"""
    )


def make_th(field):
    return f"<th>{field}</th>"


def make_td(field):
    return "<td>{{object." + field + "}}</td>"


def default_join(list):
    return "\n\t\t\t\t\t".join(list)
