

from glbase3 import *

data = genelist(filename="RBPDB_v1.3.1_proteins_mouse_2012-11-21.csv", format={"ensg": 1, "name": 4, "domain": 8, "skiplines": -1})

eurbpdb = genelist(filename='EuRBPDB/Mus_musculus.RBP.txt.gz', gzip=True,
    format={'skiplines': -1, 'force_tsv': True, 'ensg': 0, 'name': 1, 'domain': 5})

print(data)

data = data + eurbpdb

data = data.removeDuplicates('ensg')

data.saveTSV("RBP_mm10.tsv", key_order=["ensg", "name", "domain"])
data.save("RBP_mm10.glb")
