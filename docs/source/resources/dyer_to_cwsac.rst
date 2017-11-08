#############
dyer_to_cwsac
#############

:name: dyer_to_cwsac
:path: dyer_to_cwsac.json
:format: json

This provides mappings between ``dyer_engagements`` and CWSAC IDs.
These are mostly one CWSAC battle to many Dyer engagements. However, this
is difficult since Dyer engagements themselves can be subsets of other
engagements, notably sieges. These mappings are not complete because I
haven't figured out a good data model for the relationships yet.  The intended
use is constructing estimates of casualties for CWSAC definitions of battles.

Sources:
