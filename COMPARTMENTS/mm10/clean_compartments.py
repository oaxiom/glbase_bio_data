
"""

clean compartments

"""

import os, operator
from glbase3 import *

os.system('wget -c https://download.jensenlab.org/mouse_compartment_integrated_full.tsv')

comparts_to_get = ["Nucleus", "Cytoskeleton", "Plasma membrane", "Golgi apparatus", "Endosome",
    'Cytoplasm', 'Lysosome', 'Mitochondrion', ]

comparts = {}
cindex = 0
genes = {}
oh = open("mouse_compartment_integrated_full.tsv", "rt")
for lin in oh:
    lin = lin.strip().split("\t")

    if lin[1] not in genes:
        genes[lin[1]] = {"name": lin[1], "ensp": lin[0], "conditions": []}

    # There are hundreds of compartments, I only what a selection:
    if lin[3] not in comparts_to_get: # Here so every gene will get filled in
        continue

    if lin[3] not in comparts:
        comparts[lin[3]] = cindex
        cindex += 1

    while len(genes[lin[1]]["conditions"]) < cindex:
        genes[lin[1]]["conditions"].append(0)

    if float(lin[4]) >= 3: # Only use >3 confidence
        genes[lin[1]]["conditions"][comparts[lin[3]]] = int(float(lin[4]))

oh.close()

# Fill in any missing entries in "conditions"
for gene in genes:
    while len(genes[gene]["conditions"]) < cindex:
        genes[gene]["conditions"].append(0)

conds = zip(comparts.keys(), comparts.values())
conds = sorted(conds, key=operator.itemgetter(1))
print(conds)
conds = [i[0] for i in conds]

expn = expression(loadable_list=[genes[k] for k in genes], cond_names=conds)
expn.saveTSV("mm10_compartments_selected.tsv", key_order=["name"])
expn.save("mm10_compartments_selected.glb")

print(expn)

expn.heatmap(filename="compartments.png", bracket=[0, 5], col_cluster=False)

