

from glbase3 import *

mapper = glload(os.path.join(os.path.expanduser("~"), "hg38/hg38_ensembl_v94-ensg.glb"))
go = genelist(filename="20140710_gene_association.goa_ref_human", format={"force_tsv": True, "name": 2, "GO": 4, "commentlines": "!"})

print(go)

gos_todo = {"GO:0005856": "cytoskeleton",
    "GO:0015629": "actin cytoskeleton",
    "GO:0045111": "intermediate filament cytoskeleton",
    "GO:0015630": "microtubule cytoskeleton",
    "GO:0048870": "cell motility",
    "GO:0030036": "actin cytoskeleton organization",
    "GO:0004888": "transmembrane signaling receptor activity",
    # CC terms for SNX16:
    "GO:0005634": "nucleus",
    "GO:0005764": "lysosome",
    "GO:0005769": "early endosome",
    "GO:0005770": "late endosome",
    "GO:0005768": "endosome",
    "GO:0010008": "endosome membrane",
    "GO:0015629": "actin cytoskeleton",
    "GO:0005886": "plasma membrane",
    "GO:0005794": "Golgi apparatus",
    "GO:0005783": "endoplasmic reticulum",
    "GO:0005829": "cytosol",
    "GO:0005777": "peroxisom",
    "GO:0005874": "microtubule",
    "GO:0001837": "EMT",
    "GO:0060231": "MET",
    'GO:0006633': 'Fatty acid biosynthetic process',
    # Just checking:
    "GO:0032502": "Developmental processes",
    'GO:0043966': 'Histone H3 acetylation', 
    }

for g in gos_todo:
    gos = go.get(key="GO", value=g)
    
    gos = gos.map(genelist=mapper, key="name").removeDuplicates("ensg")
    
    gos.saveTSV("%s_%s.tsv" % (g.replace(":", "-"), gos_todo[g]))
    gos.save("glbs/%s_%s.glb" % (g.replace(":", "-"), gos_todo[g]))