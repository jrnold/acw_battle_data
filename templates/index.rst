{{ '#' * title|length }}
{{ title }}
{{ '#' * title|length }}

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})		    
:Homepage: {{ homepage }}
		    
{{ description }}

*keywords:* {{ keywords|join(', ') }}

## Downloads

- `acw_battle_data-{{version}}.tar.gz <https://s3.amazonaws.com/{{aws_bucket}}/aws_battle_data/aws_battle_data-{{version}}.tar.gz>`__
- `acw_battle_data-{{version}}.zip <https://s3.amazonaws.com/{{aws_bucket}}/aws_battle_data/aws_battle_data-{{version}}.zip>`__


.. toctree::
   :maxdepth: 1
   :glob:
   :includehidden:

   *

.. toctree::
   :glob:
   :hidden:

   resources/*
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
	   
