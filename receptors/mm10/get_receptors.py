
"""

Get and arrange cytokine families

Based on The cytokine family database - Chemokines

"""

import sys, os
from glbase3 import *

user_path = os.path.expanduser("~")
ems = glload(os.path.join(user_path, "mm10", "mm10_ensembl_v79_ensg.glb")).removeDuplicates("ensg")
CDs = glload('../../CD/mm10_CD_map.glb')

Families = { # taken from big_tree
    "Hematopoietin_family": ems.getRowsByKey(key="name", values="Il[2-6]r[a-g]$|Il7r$|Il9r|Il11ra[1-2]|Il1[2-3]r[a-b][1-2]|Il15ra|Il21r|Il6st|Lifr$|Osmr$|Lepr$|Crlf2|Epor|Ghr$|Prlr$|Mpl$|Cntfr|Csf[23]r"),
    "Interferon_interleukin_family": ems.getRowsByKey(key="name", values="Ifn[agl]r[1-2]|Il10r[a-b]|Il20r[a-b]|Il22ra|Il28ra"),

    # TGFb types (Set/ThrK)
    "TGFb_type1": ems.getRowsByKey(key="name", values="Tgfbr1$|Bmpr1[a-b]|Acvr1$|Acvr11$|Acvr1b$"),
    "TGFb_type2": ems.getRowsByKey(key="name", values="Acvr2a|Acvr2b|Tfgbr2$|Bmpr2|Amhr2"),

    # Receptor tyrK: taken from KEGG:
    "EGF_family": ems.getRowsByKey(key="name", values="Egfr$|Erbb[2-4]$"), # Class 1
    "Insulin_family": ems.getRowsByKey(key="name", values="Insr$|Insrr|Igf1r|Ros1$"), # Class 2
    "PDGF_family": ems.getRowsByKey(key="name", values="Pdgfr[abl]|Kit$|Flt3$|Csf1r$"), # Class 3
    "FGF_family": ems.getRowsByKey(key="name", values="Fgfr[0-9]$|Fgfr[0-9][0-9]$"), # Class 4
    "VEGF_family": ems.getRowsByKey(key="name", values="Flt1$|Flt4$|Kdr$"), # Class 5
    "HGF_family": ems.getRowsByKey(key="name", values="Met$|Mst1r$"), # Class 6
    "Neurotrophic_family": ems.getRowsByKey(key="name", values="Ntrk[1-3]$"), # Class 7
    "Ephin_family": ems.getRowsByKey(key="name", values="Epha[1-8]$|Ephb[1-6]"), # Class 8
    "AXL_family": ems.getRowsByKey(key="name", values="Axl$|Tyro3$|Mertk$"), # Class 9
    "LTK_family": ems.getRowsByKey(key="name", values="Ltk$|Alk$"), # Class 10
    "TIE_family": ems.getRowsByKey(key="name", values="Tie1$|Tek$"), # Class 11
    "ROR_family": ems.getRowsByKey(key="name", values="Ror[1-2]$"), # Class 12
    "DDR_family": ems.getRowsByKey(key="name", values="Ddr[1-2]$"), # Class 13
    "RTyrK_others": ems.getRowsByKey(key="name", values="Ret$|Ptk7$|Ryk$|Musk$|Aatk|Lmtk2|Lmtk3"), # Class 14-17 and unassigned PRTyK.

    # TNF family:
    "TNF_family": ems.getRowsByKey(key="name", values="Tnfrsf|Ngfr|Relt|Edar$|Edar2r|Cd27$|Cd40$|Ltbr|Fas$"),

    # IL-1
    "Interleukin1_family": ems.getRowsByKey(key="name", values="Il1r[12]|Il1rl[12]|Il18r1|Sigirr|Il1rap|Il18rap|Il1rapl[12]"),

    #Il17
    "Interleukin17_family": ems.getRowsByKey(key="name", values="Il17r[a-e]"),

    # Chemokines:
    "Chemokine_CC": ems.getRowsByKey(key="name", values="Ccr[1-9]$|Ccr10|Ccr12|Ccrl[12]|Ackr[124]"), # http://en.wikipedia.org/wiki/CC_chemokine_receptors, this should probably be a training set.
    "Chemokine_CXC": ems.getRowsByKey(key="name", values="Cxcr[1-9]|Cxcr1[0-9]|Ackr3"),
    "Chemokine_other": ems.getRowsByKey(key="name", values="Cx3cr1|Xcr1|Cmklr1|Gper1|Ptgdr2$"),

    # These all need to be added into the cytokines...
    "Gpr_Fzd": ems.getRowsByKey(key="name", values="Fzd[1-9]|Smo$"),
    "Gpr_Neuropeptides": ems.getRowsByKey(key="name", values="Tacr[1-3]|Ntsr[12]|Ghsr|Galr[1-3]|Mchr1|Hcrtr[12]|Nmur[12]|Nmbr$|Npy[1-6]|Npbwr1|Npffr[12]|Npsr1|Oprd[dkml]1|Nmbr$|Grpr$|Brs3$|Fpr[123]|Qrfpr|C130060K24Rik"),
    "Gpr_Cardiovascular_peptide": ems.getRowsByKey(key="name", values="Agtr[12][ab]|Bdkrb[12]|Ednr[ab]|Uts2r"),
    "Gpr_Pituitary": ems.getRowsByKey(key="name", values="Tshr|Lhcgr|Fshr"),
    "Gpr_Relaxins": ems.getRowsByKey(key="name", values="Rxfp[1234]"),
    "Gpr_Gut_peptide": ems.getRowsByKey(key="name", values="Cck[ab]r|Aplnr|Prokr[12]"),
    "Gpr_vision": ems.getRowsByKey(key="name", values="Rho$|Opn1sw|Opn1mw|Opn[345]$|Rrh$|Rgr$"),
    "Gpr_secretin": ems.getRowsByKey(key="name", values="Calcr|Pth[12]r|Crhr[12]|Ghrhr|Adcyap1r1|Gipr|Vipr[12]|Sctr|Emr[14]|Cd97|Lphn[123]|Eltd1|Bai[123]|Ramp[123]"),
    "Gpr_others": ems.getRowsByKey(key="name", values="Gpr[1-9]|Gprc[5-6]|Gprin[1-3]|Ptafr|Mas1$|Mrgpr[defg]|Mrgpr[axb][129]$|Lgr[456]"),
    "Gpr_endothelins": ems.getRowsByKey(key="name", values="Ednr[a-b]|Dear1"),

    # Other non-KEGG annotated enzymes
    "GDNF_receptors": ems.getRowsByKey(key="name", values="Gfra[1-4]|Gfral"),

    "CCN_target_receptors":  ems.getRowsByKey(key="name", values="Itga|Itgb[1-9]$|Ldlr"), #CCN can bind to integrins and Ldlr
    "CDs": CDs.map(genelist=CDs, key='name')
    }

for k in Families:
    Families[k].saveTSV("mm10_%s.tsv" % k, key_order=["ensg", "enst", "name"])
    Families[k] = genelist(filename="mm10_%s.tsv" % k, format={"ensg":0, "enst":1, "name":2, "force_tsv": True}) # A bunch of junk gets stored in the glb. Strip that out.
    Families[k].save("mm10_%s.glb" % k)

all = sum(list(Families.values())[1:], list(Families.values())[0])
all = all.removeDuplicates("ensg")
all.save("mm10_all_receptors.glb")
all.saveTSV("mm10_all_receptors.tsv")
