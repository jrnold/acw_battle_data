# -*- coding: utf-8 -*-

from citeproc.source.bibtex import BibTeX

from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import formatter
from citeproc import Citation, CitationItem

bib_source = BibTeX('acwbd.bib')

bib_style = CitationStylesStyle('harvard1', validate=False)

bibliography = CitationStylesBibliography(bib_style, bib_source,
                                          formatter.plain)
