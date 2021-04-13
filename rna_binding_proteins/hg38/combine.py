"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

import os, sys
from glbase3 import *

rbp_form = {"force_tsv": False, "ensg": 1, 'name': 4}

dbd = genelist("RBPDB_v1.3.1_proteins_human_2012-11-21.csv.gz", format=rbp_form, gzip=True)
dbd.save('rbp_db_hg38.glb')
dbd.saveTSV('rbp_db_hg38.tsv', key_order=['ensg', 'enst', 'ensp', 'name'])

print()
print(dbd)
