

from glbase import *

mapper = glload(os.path.join(os.path.expanduser("~"), "mm9/mm9_ensembl_v67_enst_entrez.glb")).removeDuplicates("ensg")
go = genelist(filename="gene_association", format={"force_tsv": True, "name": 2, "GO": 4, "commentlines": "!"})

print go

gos_todo = {"GO:0005856": "cytoskeleton",
    "GO:0015629": "actin cytoskeleton",
    "GO:0045111": "intermediate filament cytoskeleton",
    "GO:0015630": "microtubule cytoskeleton",
    "GO:0048870": "cell motility",
    "GO:0030036": "actin cytoskeleton organization",
    "GO:0004888": "transmembrane signaling receptor activity",
    "GO:0004930": "G-protein coupled receptor activity",
    "GO:0003723": "RNA binding",
    'GO:0005125': "cytokine activity",
    "GO:0008083": "growth factor activity",
    'GO:0043235': "receptor complex",
    'GO:0045087': 'innate immune response',
    'GO:0009615': 'response to virus',
    'GO:0034341': 'response to interferon-gamma',
    'GO:0045596': 'negative regulation of cell differentiation',
    'GO:0060562': 'epithelial tube morphogenesis',
    "GO:0035295": 'tube development',
    }

for g in gos_todo:
    gos = go.get(key="GO", value=g)
    
    gos = gos.map(genelist=mapper, key="name").removeDuplicates("ensg")
    
    gos.saveTSV("%s_%s.tsv" % (g.replace(":", "-"), gos_todo[g]))
    gos.save("glbs/%s_%s.glb" % (g.replace(":", "-"), gos_todo[g]))