
"""

Get and arrange cytokine families

"""

import sys, os
from glbase3 import *

user_path = os.path.expanduser("~")
ems = glload(os.path.join(user_path, "mm10", "mm10_ensembl_v95_ensg.glb")).removeDuplicates("ensg")

Families = { # taken from big_tree
    "Interleukins": ems.getRowsByKey(key="name", values="Il[0-9][0-9]$|Il[0-9][0-9][a-f]$|Il[0-9][a-f]|Il[0-9][a-f]|Il[0-9]$|Lif$|Clcf1|Cntf$|Ctf[1-2]|Ebi3|Iltifb|Lep$|Osm$|Ppbp$"),
    "Interferons": ems.getRowsByKey(key="name", values="Ifn[a-z]$|Ifn[a-z][1-9][1-9]$|Ifn[a-z][1-9]$|Ifnab$"),
    "Endothelins": ems.getRowsByKey(key="name", values="Edn[1-3]"),
    "Bmps": ems.getRowsByKey(key="name", values="Bmp[0-9]"),
    "Egfs": ems.getRowsByKey(key="name", values="Egf$|Nrg[1-4]$|Btc$|Hbegf|Areg|Ereg|Epgn|Tdgf1$"),
    "Chemokines": ems.getRowsByKey(key="name", values="Cxcl[0-9]|Ccl[0-9][0-9]|Ccl[0-9]|Xcl[0-2]|Cx3cl1|Pf4"),
    "Chemokine-like": ems.getRowsByKey(key="name", values="Cmtm[0-9]"),
    "Tnfs": ems.getRowsByKey(key="name", values="Tnf[a-q]$|Tnf$|Lt[a-b]$|Fasl|Tnfsf|Cd40lg|Cd70"),
    "Tgfs": ems.getRowsByKey(key="name", values="Tgf[a-b]$|Tgf[a-b][0-9]$|Lefty[1-2]|Nodal|Gdnf|Nrtn"),
    "Fgfs": ems.getRowsByKey(key="name", values="Fgf[0-9]"),
    "Pdgfs": ems.getRowsByKey(key="name", values="Pdgf[a-z]$"),
    "Vegfs": ems.getRowsByKey(key="name", values="Vegf[a-z]|Figf|Pgf"), # PGF, despite the name is a VEGF
    "Gdfs": ems.getRowsByKey(key="name", values="Gdf[0-9]|Mstn"),
    "Wnts": ems.getRowsByKey(key="name", values="Wnt[0-9]"),
    "Igfs": ems.getRowsByKey(key="name", values="Igf[1-2]$"),
    "Csfs": ems.getRowsByKey(key="name", values="Csf[1-3]$"),
    "Ngf": ems.getRowsByKey(key="name", values="Gmf[b-g]|Ngf$"),
    "Inhibins": ems.getRowsByKey(key="name", values="Inh[a-b]"),
    "DAN": ems.getRowsByKey(key="name", values="Ndp$|Grem[1-2]$|Cer1$|Nbl1$|Gpha2$|Dand5$"),
    "CCN": ems.getRowsByKey(key="name", values="Ctgf|Nov$|Wisp[1-3]$|Cyr61$"),
    "Neuregulin": ems.getRowsByKey(key="name", values="Nrg[1-4]"),
    "Peptide_hormones": ems.getRowsByKey(key="name", values="Calca|Calcb|Pth|Gast$|Ghrl$|Gal$|Penk$|Npy|Sst$|Cck$|Vip$|Tac[124]|Nts$|Trh$|Lhb$|Cga$|Fshb$|Avp$|Pmch$|Hcrt|Nm[bsu]$|Apln$|Uts2|Rln[13]"),
    }

for k in Families:
    Families[k].saveTSV("mm10_%s.tsv" % k, key_order=["ensg", "enst", "name"])
    Families[k] = genelist(filename="mm10_%s.tsv" % k, format={"ensg":0, "enst":1, "name":2, "force_tsv": True}) # A bunch of junk gets stored in the glb. Strip that out.
    Families[k].save("mm10_%s.glb" % k)

all = sum(list(Families.values())[1:], list(Families.values())[0])
all = all.removeDuplicates("ensg")
all.save("mm10_all_cytokines.glb")
all.saveTSV("mm10_all_cytokines.tsv")
