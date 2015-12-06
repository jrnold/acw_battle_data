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
{% if field.constraints is defined %}
    {% if "required" in field.constraints %}:required: {{field.constraints.required}} {% endif %}
    {% if "minLength" in field.constraints %}:minLength: {{field.constraints.minLength}} {% endif %}
    {% if "maxLength" in field.constraints %}:maxLength: {{field.constraints.maxLength}} {% endif %}
    {% if "unique" in field.constraints %}:unique: {{field.constraints.unique}} {% endif %}
    {% if "pattern" in field.constraints %}:pattern: {{field.constraints.pattern}} {% endif %}
    {% if "minimum" in field.constraints %}:minimum: {{field.constraints.minimum}} {% endif %}
    {% if "maximum" in field.constraints %}:maximum: {{field.constraints.maximum}} {% endif %}
    {% if "enum" in field.constraints %}:enum: {{field.constraints.enum}} {% endif %}     
{% endif %}

{{ field.description }}
       
{% endfor %}
{% endif %}
