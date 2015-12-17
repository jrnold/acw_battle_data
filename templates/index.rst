{{ '#' * title|length }}
{{ title }}
{{ '#' * title|length }}

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})		    
:Homepage: {{ homepage }}
		    
{{ description }}

*keywords:* {{ keywords|join(', ') }}


.. toctree:: Table of Contents
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
	   
