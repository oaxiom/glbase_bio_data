

from glbase import *

mapper = glload(os.path.join(os.path.expanduser("~"), "mm9/mm9_ensembl_v67_enst_entrez.glb")).removeDuplicates("ensg")
go = genelist(filename="gene_association", format={"force_tsv": True, "name": 2, "GO": 4, "commentlines": "!"})

gos_todo = ["GO:0051327"]

for g in gos_todo:
    print g
    gos = go.get(key="GO", value=g)
    
    print gos
    
    gos = gos.map(genelist=mapper, key="name").removeDuplicates("ensg")
    
    print g, len(gos)