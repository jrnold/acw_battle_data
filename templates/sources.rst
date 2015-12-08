############
Sources
############

{% for cit in sources|dictsort %}
.. [{{cit[0]}}] {{cit[1].text}} {{cit[1].url}}
{% endfor %}
  
