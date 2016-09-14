{{ '#' * title|length }}
{{ title }}
{{ '#' * title|length }}

:Version: {{ version }}
:License: `{{ license.type }} <{{license.url}}>`__
:Author: {{ author.name }} <{{author.email}}> ({{author.web}})
:Homepage: {{ homepage }}

{{ description }}

*keywords:* {{ keywords|join(', ') }}

Downloads

- `acw_battle_data-{{version}}.tar.gz <https://{{aws_bucket}}.s3.amazonaws.com/acw_battle_data/acw_battle_data-{{version}}.tar.gz>`__
- `acw_battle_data-{{version}}.zip <https://{{aws_bucket}}.s3.amazonaws.com/acw_battle_data/acw_battle_data-{{version}}.zip>`__


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
