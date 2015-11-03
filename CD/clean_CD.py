"""

Clean CD numbers

"""

from glbase import *

CD = genelist(filename="List_of_Cluster_of_Differentiation_genes.txt", format={"CD": 0, "name": 1, "skiplines": 0, "force_tsv": True})

print CD

# First get the human as the CD gene names are primarily human.
hg19 = glload(os.path.expanduser("~/hg19/hg19_ensembl_v73-ensg-entrez.glb"))

hCD = CD.map(genelist=hg19, key="name").removeDuplicates("ensg")
hCD.saveTSV("hg19_CD_map.tsv", key_order=["ensg", "name"])
hCD.save("hg19_CD_map.glb")
print hCD

# Now do the mouse:
CD = genelist(filename="List_of_Cluster_of_Differentiation_genes.txt", format={"CD": 0, "name": 2, "skiplines": 0, "force_tsv": True}).removeDuplicates("name")

mm9 = glload(os.path.expanduser("~/mm9/mm9_ensembl_v67_enst_entrez.glb"))

mCD = CD.map(genelist=mm9, key="name").removeDuplicates("ensg")
mCD.saveTSV("mm9_CD_map.tsv", key_order=["ensg", "name"])
mCD.save("mm9_CD_map.glb")
print hCD