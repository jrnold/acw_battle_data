{{ '#' * title|length }}
{{ title }}
{{ '#' * title|length }}

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})		    
:Homepage: {{ homepage }}
		    
{{ description }}

*keywords:* {{ keywords|join(', ') }}

{% if sources|length %}
**Sources:**
{% for src in sources -%}
- {{src.name}}{% if src.url is defined %}; {{src.url}}{% endif %}{% if src.email is defined %}; {{src.email}}{% endif %}
{% endfor -%}
{% endif %}

.. toctree::
   :caption: Resources
   :maxdepth: 1
   :glob:
   
   resources/*
       

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
	   
