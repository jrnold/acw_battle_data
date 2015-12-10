{{ '#' * title|length }}
{{ title }}
{{ '#' * title|length }}

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})		    
:Homepage: {{ homepage }}
		    
{{ description }}

*keywords:* {{ keywords|join(', ') }}

Resources
=========

.. toctree::
   :maxdepth: 1
   :glob:
   
   resources/*

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:
   
   *
   

Indices and tables
==================

* :doc:`Sources`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
	   
