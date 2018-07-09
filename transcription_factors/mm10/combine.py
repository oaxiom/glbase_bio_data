
"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

from glbase3 import *

map_form = {"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3}

mapper = genelist(os.path.join(os.path.expanduser("~"), "mm10/mm9.ensg.enst.ensp.name.v67.tsv"), format=map_form)

tfdbd_form = {"force_tsv": True, "ensp": 1}
anitf_form = {"force_tsv": True, "ensg": 1, "name": 3}

tfdbd = genelist("TFDBD_table.tsv", format=tfdbd_form)
tfdbd.save("all_tfdbd.glb")
tfcla = glload("TFClass.mm9.glb")
anitf = genelist("AnimalTFDB.tsv", format=anitf_form)

# map all relative to ensg:
tfdbd = mapper.map(tfdbd, key="ensp").removeDuplicates("ensg")

all_tfs = tfdbd + tfcla + anitf
all_tfs = all_tfs.removeDuplicates("ensg")

all_tfs = all_tfs.getColumns(["ensg", "name"])
all_tfs.sort("name")
all_tfs.saveTSV("all_tfs.tsv")
all_tfs.save("all_tfs.glb")

print("Finally", len(all_tfs), "tfs")

gl = glglob(tfdbd, tfcla, anitf)
gl.venn(filename="overlap.png", key="ensg")