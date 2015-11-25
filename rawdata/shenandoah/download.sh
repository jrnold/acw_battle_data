#!/bin/bash
# Download the entire report
wget -r -D http://www.nps.gov/abpp/shenandoah/svs0-1.html
wget -r -l 1 -A svs*-*.html http://www.nps.gov/abpp/shenandoah/svs0-1.html
wget -r -l 1 -A svsfig*.html http://www.nps.gov/abpp/shenandoah/svs0-1.html
wget -r -l 1 -A svstab*.html http://www.nps.gov/abpp/shenandoah/svs0-1.html
