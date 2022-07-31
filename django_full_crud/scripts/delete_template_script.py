def delete_template_script():
    return """{% extends 'base.html' %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        <p>Tem certeza que deseja deletar {{object}}?</p>
        <a href="javascript:window.history.back();">Cancelar</a>
        <button type="submit">Apagar</button>
    </form>
{% endblock %}
"""
