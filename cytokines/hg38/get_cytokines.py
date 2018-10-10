
"""

Get and arrange cytokine families

"""

import sys, os
from glbase import *

user_path = os.path.expanduser("~")
ems = glload(os.path.join(user_path, "hg19", "hg19_ensembl_v74-ensg-entrez.glb")).removeDuplicates("ensg")

Families = { # taken from big_tree
    "Interleukins": ems.getRowsByKey(key="name", values="IL[0-9][0-9]$|IL[0-9][0-9][A-F]|IL[0-9][A-F]|IL[0-9][A-F]|IL[0-9]$|LIF$|CLCF1$|CNTF$|CTF[1-2]|EBI3|ILTIFB|LEP$|OSM$"),
    "Interferons": ems.getRowsByKey(key="name", values="IFN[A-Z]$|IFN1[A-Z]$|IFNAB$"), # THis line is worng?!?! See the mouse table.
    "Endothelins": ems.getRowsByKey(key="name", values="EDN[1-3]"),
    "Bmps": ems.getRowsByKey(key="name", values="BMP[0-9]"),
    "Egfs": ems.getRowsByKey(key="name", values="EGF$|NRG[1-4]$|BTC$|HBEGF|AREG|EREG|EPGN|TDGF1"),
    "Chemokines": ems.getRowsByKey(key="name", values="CXCL[0-9]|CCL[0-9][0-9]$|CCL[0-9]$|XCL[0-2]$|CX3CL1$|^PF4$"),
    "Chemokine-like": ems.getRowsByKey(key="name", values="CMTM[0-9]"),
    "Tnfs": ems.getRowsByKey(key="name", values="TNF[A-Q]$|TNF$|LT[A-B]$|FASL"),
    "Tgfs": ems.getRowsByKey(key="name", values="TGF[A-B]$|TGF[A-B][0-9]$|LEFTY[1-2]|NODAL|GDNF|NRTN"),
    "Fgfs": ems.getRowsByKey(key="name", values="FGF[0-9]$|FGF[1-2][0-9]$"),
    "Pdgfs": ems.getRowsByKey(key="name", values="PDGF[A-Z]$|PGF"),
    "Vegfs": ems.getRowsByKey(key="name", values="VEGF[A-Z]|FIGF"),    
    "Gdfs": ems.getRowsByKey(key="name", values="GDF[0-9]|MSTN"),
    "Wnts": ems.getRowsByKey(key="name", values="WNT[0-9]$|WNT[0-9][A-E]$|WNT1[0-9]$|WNT1[0-9][A-F]$"),
    "Igfs": ems.getRowsByKey(key="name", values="IGF[1-2]$"),
    "Csfs": ems.getRowsByKey(key="name", values="CSF[1-3]$"),
    "Ngf": ems.getRowsByKey(key="name", values="GMF[B-G]|NGF$"),
    "Inhibins": ems.getRowsByKey(key="name", values="INH[A-B]$|INHB[A-E]$"),
    "DAN": ems.getRowsByKey(key="name", values="NDP$|GREM[1-2]$|^CER1"), # See the mouse for updates
    "CCN": ems.getRowsByKey(key="name", values="CTGF|NOV$|WISP[1-3]$"),
    "Neuregulin": ems.getRowsByKey(key="name", values="NRG[1-4]$"),
    "Other":  ems.getRowsByKey(key="name", values="^NOG$"),
    }

for k in Families:
    if Families[k]:
        Families[k].saveTSV("hg19_%s.tsv" % k, key_order=["ensg", "name"])
        Families[k] = genelist(filename="hg19_%s.tsv" % k, format={"ensg":0, "name":1, "force_tsv": True}) # A bunch of junk gets stored in the glb. Strip that out.
        Families[k].save("hg19_%s.glb" % k)
    else:
        print ">>> %s empty!" % k

all = sum(Families.values()[1:], Families.values()[0])
all = all.removeDuplicates("ensg")
all.saveTSV("all.ensg.tsv", key_order=["name"])
all.save("all.ensg.glb")