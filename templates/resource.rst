{{ title }}
================================================================================

:name: {{ name }}
:path: {{ path }}
:format: {{ format }}

{{ description }}

{% if format is equalto 'csv' %}
Schema
-------

{%if schema.primaryKey %}:Primary Key:{{ schema.primaryKey }}{% endif %}
{%if schema.foreignKeys %}:Foreign Keys:
{% for fk in schema.foreignKeys %}
    :{{ fk.fields|join(', ') }}: {{fk.reference.datapackage}}, {{fk.reference.resource}}, {{fk.reference.fields|join(', ')}}
{% endfor %}
{% endif %}

{% for field in schema.fields %}
{{ field.name }}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: {{ field.label }}
:type: {{field.type }}
{% if field.format %}:format: {{field.format}} {% endif %}
{% if field.constraints %}
    {% if field.constraints.required %}:required: {{field.constraints.required}} {% endif %}
    {% if field.constraints.minLength %}:minLength: {{field.constaints.minLength}} {% endif %}
    {% if field.constraints.maxLength %}:maxLength: {{field.constaints.maxLength}} {% endif %}
    {% if field.constraints.unique %}:unique: {{field.constaints.unique}} {% endif %}
    {% if field.constraints.pattern %}:pattern: {{field.constaints.pattern}} {% endif %}
    {% if field.constraints.minimum %}:minimum: {{field.constaints.minimum}} {% endif %}
    {% if field.constraints.maximum %}:maximum: {{field.constaints.maximum}} {% endif %}
    {% if field.constraints.enum %}:enum: {{field.constaints.enum}} {% endif %}     
{% endif}

{{ field.description }}
       
{% endfor %}
{% endif %}
