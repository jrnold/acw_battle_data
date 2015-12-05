# {{ title }}

{{ description }}

<table>
<tr>
<th>Name</th>
<th>Path</th>
<th>Title</th>
</tr>
{% for res in resources %}
<tr>
<td>{{ res.name }}</td>
<td>{{ res.path }}</td>
<td>{{ res.title }}</td>
</tr>
{% endfor %}
</table>

