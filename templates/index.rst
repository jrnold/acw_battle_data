{{ title }}
================================================================================

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})		    
:Homepage: {{ homepage }}
		    
{{ description }}

*keywords:* {{ keywords|join(', ') }}

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
	   
