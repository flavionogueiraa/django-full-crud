def detail_template_script(class_info):
    fields = list(map(make_field, class_info["fields_name"]))

    return (
        """{% extends 'base.html' %}

{% block content %}
    <div>
        <h1>Detalhes de """ + class_info["class_verbose_name"] + """</h1>
        <div>
            """ + default_join(fields) + """
        </div>
    </div>
{% endblock %}
"""
    )

def make_field(field):
    return "<div>{{object." + field + "}}</div>"


def default_join(list):
    return "\n\t\t\t".join(list)
