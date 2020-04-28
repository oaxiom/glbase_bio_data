"""

process the Animal TFDB data which is a bloody mess.

"""

import sys, os
from glbase3 import *

map_form = {"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3}
mapper = genelist(os.path.join(os.path.expanduser("~"), "mm10/mm10_ensg.enst.ensp.name.v99.tsv"), format=map_form)

oh = open("AnimalTFDB.raw.txt", "rt")

res = []
for line in oh:
    tt = line.split()
    print(tt)
    res.append({"ensg": tt[0]})

oh.close()

gl = genelist()
gl.load_list(res)

print(gl)

gl = gl.map(genelist=mapper, key="ensg").removeDuplicates("ensg")
gl.saveTSV("AnimalTFDB.tsv", key_order=['ensg'])
