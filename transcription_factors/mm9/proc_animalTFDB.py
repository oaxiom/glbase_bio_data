"""

process the Animal TFDB data which is a bloody mess.

"""

from glbase import *

map_form = {"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3}
mapper = genelist(os.path.join(os.path.expanduser("~"), "mm9/mm9.ensg.enst.ensp.name.v67.tsv"), format=map_form)

oh = open("AnimalTFDB.raw.txt", "rU")

res = []
for line in oh:
    tt = line.split()
    res.append({"ensg": tt[1]})
    
oh.close()

gl = genelist()
gl.load_list(res)

print gl

gl = gl.map(genelist=mapper, key="ensg").removeDuplicates("ensg")
gl.saveTSV("AnimalTFDB.tsv")