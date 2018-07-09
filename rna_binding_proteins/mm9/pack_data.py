

from glbase import *

data = genelist(filename="RBPDB_v1.3.1_proteins_mouse_2012-11-21.csv", format={"ensg": 1, "name": 4, "domain": 8, "skiplines": -1})

print data

data = data.removeDuplicates('ensg')

data.saveTSV("RBP_mm9.tsv", key_order=["ensg", "name", "domain"])
data.save("RBP_mm9.glb")