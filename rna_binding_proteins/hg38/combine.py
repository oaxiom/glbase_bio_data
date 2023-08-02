"""

Merge RBP databases

"""

import os, sys
from glbase3 import *

eurbpdb = genelist(filename='EuRBPDB/Homo_sapiens.RBP.txt.gz', gzip=True,
    format={'skiplines': -1, 'force_tsv': True, 'ensg': 0, 'name': 1, 'domain': 4})

dbd = genelist("RBPDB_v1.3.1_proteins_human_2012-11-21.csv.gz",
    format={"force_tsv": False, "ensg": 1, 'name': 4, 'domain': 8},
    gzip=True)

data = dbd + eurbpdb
data = data.removeDuplicates('ensg')

data.save('rbp_db_hg38.glb')
data.saveTSV('rbp_db_hg38.tsv', key_order=['ensg', 'name', 'domain'])

