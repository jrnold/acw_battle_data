def doctable(table, title = False):
    """ String to document a Table object """
    def _colstring(col):
        data = {'colname' : col.name,
                'coltype' : col.type,
                'coldoc' : col.doc if col.doc else ''}
        return(":{colname}: {coltype}, {coldoc}".format(**data))
    template = "\n{doc}\n\n{columns}"
    if title:
        template = "{tablename}\n{underline}\n" + template
    data = {'tablename' : table.name,
            'doc' : table.info['doc'] if 'doc' in table.info else '',
            'underline' : '-' * len(table.name),
            'columns' : '\n'.join([_colstring(col) for col in table.c])}
    return template.format(**data)
