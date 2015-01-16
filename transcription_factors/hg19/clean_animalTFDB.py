"""

process the Animal TFDB data which is a bit of a mess (better than mouse for some reason).

"""

from glbase import *

mapper = glload(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-entrez.glb"))

oh = open("AnimalTFDB.raw.txt", "rU")

res = []
for line in oh:
    tt = line.split()
    res.append({"ensg": tt[0]})
    
oh.close()

gl = genelist()
gl.load_list(res)

print gl

gl = gl.map(genelist=mapper, key="ensg").removeDuplicates("ensg")
gl.saveTSV("AnimalTFDB.tsv")