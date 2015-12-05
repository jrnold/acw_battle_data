# {{ Resources }}

<table>
<tr>
<th>Name</th>
<th>Path</th>
<th>Title</th>
</tr>
{% for res in resources %}
<tr>
<td><a href="{{ "resources/%s.html"|format(res.name) }}">{{ res.name }}</a></td>
<td>{{ res.path }}</td>
<td>{{ res.title }}</td>
</tr>
{% endfor %}
</table>

