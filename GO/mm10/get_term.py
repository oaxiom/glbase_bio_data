
import sys, os
from glbase3 import *

mapper = glload(os.path.join(os.path.expanduser("~"), "mm10/mm10_ensembl_v95_ensg.glb"))
go = genelist(filename="mgi.gaf.gz", format={"force_tsv": True, "name": 2, "GO": 4, "commentlines": "!"}, gzip=True)

print(go)

gos_todo = {
    'GO:0034341': 'response to interferon-gamma',
    'GO:0045596': 'negative regulation of cell differentiation',
    'GO:0060562': 'epithelial tube morphogenesis',
    "GO:0035295": 'tube development',
    "GO:0032502": "Developmental processe",
    'GO:0034341': 'Response to interferon-gamma',
    'GO:0035456': 'Response to interferon-beta',
    'GO:0070875': 'positive regulation of glycogen metabolic process', # Obselete term?
    'GO:0045725': 'positive regulation of glycogen biosynthetic process',
    'GO:0010506': 'Regulation of autophagy',
    'GO:0034470': 'ncRNA processing',
    'GO:0022613': 'ribonucleoprotein complex biogenesis',
    'GO:0042254': 'ribosome biogenesis',
    'GO:0022904': 'respiratory electron transport chain',
    }

for g in gos_todo:
    print(g)
    gos = go.get(key="GO", value=g)

    if gos:
        gos = gos.map(genelist=mapper, key="name").removeDuplicates("ensg")

        gos.saveTSV("%s_%s.tsv" % (g.replace(":", "-"), gos_todo[g]))
        gos.save("glbs/%s_%s.glb" % (g.replace(":", "-"), gos_todo[g]))
