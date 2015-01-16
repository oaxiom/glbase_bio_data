"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

from glbase import *

ensp_m = genelist(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-enst-ensp-name.tsv"), 
    format={"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3})
mapper = glload(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-entrez.glb"))

print mapper

tfdbd_form = {"force_tsv": True, "ensp": 1}
tfcls_form = {"force_tsv": True, "ensg": 0}
anitf_form = {"force_tsv": True, "ensg": 1, "name": 3}

tfdbd = genelist("hs.tf.ass", format=tfdbd_form)
tfcls = genelist("TFClass.clean.tsv", format=tfcls_form)
anitf = genelist("AnimalTFDB.tsv", format=anitf_form)

# map all relative to ensg:
tfdbd = ensp_m.map(tfdbd, key="ensp").removeDuplicates("ensg")

all_tfs = tfdbd + tfcls + anitf
all_tfs = all_tfs.removeDuplicates("ensg")
all_tfs = all_tfs.map(genelist=mapper, key="ensg")

all_tfs = all_tfs.getColumns(["ensg", "name"])
all_tfs.sort("name")
all_tfs.saveTSV("all_tfs.tsv")
all_tfs = genelist(filename="all_tfs.tsv", format={"force_tsv": True, "ensg": 0, "name": 1})
all_tfs.save("all_tfs.glb")

print "Finally", len(all_tfs), "tfs"

gl = glglob(tfdbd, tfcls, anitf)
gl.venn(filename="overlap.png", key="ensg")