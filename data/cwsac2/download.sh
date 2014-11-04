#!/bin/bash
## Download all CWSAC Report Update pdfs from  http://www.nps.gov/hps/abpp/CWSII/CWSIIStateReports.htm
## and convert to text files
cd reports
xargs --arg-file ../CWSACII.txt wget
find . -name \*.pdf -print0 | xargs --null -I '{}' pdftotext '{}'
