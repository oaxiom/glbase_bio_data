
import os
from glbase import *

tfclass = genelist(filename="../hg19/TFclass.table.Hs.tsv", format={k[1]:k[0] for k in enumerate(["name", "ensg", "label", "id", "class_id", "combined_family", "family_id"])})

mm9hg19 = genelist(filename=os.path.expanduser("~/mm9/mm9.hg19.ensg.ensmusg.76.txt"), format={"force_tsv": True, "ensg": 1, "mmensg": 0})

print mm9hg19

tfclass = tfclass.map(genelist=mm9hg19, key="ensg").removeDuplicates("mmensg")
tfclass = tfclass.renameKey("mmensg", "ensg", replace_exisiting_key=True)
tfclass.saveTSV("TFClass.mm9.tsv", key_order=["name", "ensg", "label", "id", "combined_family"])
tfclass.save("TFClass.mm9.glb")
