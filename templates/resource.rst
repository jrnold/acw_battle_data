{{ title }}
================================================================================

:name: {{ name }}
:path: {{ path }}
:format: {{ format }}

{{ description }}

{% if format is equalto 'csv' %}
Schema
-------

{% for field in schema.fields %}
{{ field.name }}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: {{ field.label }}
:type: {{field.type }}

{{ field.description }}
       
{% endfor %}
{% endif %}
