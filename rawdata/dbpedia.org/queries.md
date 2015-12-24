
## Units

Overall category

`Military_units_and_formations_of_the_American_Civil_War`. I haven't found a good way to filter actual resources of units. Using `yago:Unit*` does not work and is too narrow.

Confederate Units. Needs to be filtered for only units. 

``` spaqrql
select distinct ?unit where {
  ?unit dct:subject/skos:broader* dbc:Military_units_and_formations_of_the_Confederate_States_Army .
}

```

Union units. Needs to be filtered for 

``` sparql
select distinct ?unit where {
  ?unit dct:subject/skos:broader* dbc:Military_units_and_formations_of_the_Union_Army
}
```

Irregular Units

``` sparql
select distinct ?unit where {
  ?unit dct:subject/skos:broader* dbc:Irregular_forces_of_the_American_Civil_War
}

```

Lists of Military_units_and_formations_of_the_Confederate_States_Army .

## Ship

``` sparql
select distinct ?ship where {
?ship dct:subject/skos:broader* dbc:Ships_of_the_Union_Navy
}
```

``` sparql
select distinct ?ship where {
?ship dct:subject/skos:broader* dbc:Ships_of_the_Confederate_States_Navy
}
```

