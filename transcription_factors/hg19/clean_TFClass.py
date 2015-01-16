

"""

clean up the TFClass data set.

"""
import os
from glbase import *

oh = open("TFClass.obo.txt", "rU")

ensgs = []
chunk = None
TFfamily = {}
TFclass = {}
TFgenus = {}
TFsubfamily = {}

for line in oh: 
    if "[Term]" in line:
        # process last chunk:
        if chunk:
            if chunk["subset"] == "Class":
                TFclass[chunk["id"]] = chunk
            if chunk["subset"] == "Family":
                TFfamily[chunk["id"]] = chunk
            if chunk["subset"] == "Subfamily": 
                TFsubfamily[chunk["id"]] = chunk
            if chunk["subset"] == "Genus": 
                TFgenus[chunk["id"]] = chunk     

        chunk = {} # new chunk
    else: # append stuff to chunk.
        if "id:" in line:
            chunk["id"] = line.split()[1].strip()
        if "name:" in line:
            chunk["label"] = line.replace("name:", "").strip()
        if "def:" == line[0:4]:
            chunk["def"] = line.replace("def:", "").strip().replace('"', '')
        if "subset:" in line:
            chunk["subset"] = line.replace("subset:", "").strip()
        if "xref" in line:
            if "ENSEMBL" in line:
                ref = line.strip().split(":")[2].split()[0]
                chunk["ensg"] = ref
    
    # Do the traditional clean-up; i.e. just get the ENSG numbers
    if "xref" in line:
        if "ENSEMBL" in line:
            ref = line.strip().split(":")[2].split()[0]
            ensgs.append(ref)
    
oh.close()        

gl = genelist()
gl.load_list([{"ensg": i} for i in ensgs])
gl = gl.removeDuplicates("ensg")
gl.saveTSV("TFClass.clean.tsv")

split_class = [
    'Tryptophan cluster factors', 
    'Basic leucine zipper factors (bZIP)',
    'High-mobility group (HMG) domain factors', 
    'Fork head / winged helix factors',
    'C2H2 zinc finger factors',
    'Nuclear receptors with C4 zinc fingers',
    'Basic helix-loop-helix factors (bHLH)',
    'Homeo domain factors']

split_family = [
    #"More than 3 adjacent zinc finger factors",
    "Factors with multiple dispersed zinc fingers"
    ]

# build a proper ENSG table.
newtab = []
for id in TFgenus:
    chunk = TFgenus[id]
    newi = {"id": chunk["id"], "label": chunk["label"]}
    if "ensg" in chunk:
        newi["ensg"] = chunk["ensg"]
    else:
        newi["ensg"] = ""
    # get the class, family, sub-family
    # Merge class, family and subfamily if present
    class_id = ".".join(chunk["id"].split(".")[0:2])
    family_id = ".".join(chunk["id"].split(".")[0:3])
    subfam_id = ".".join(chunk["id"].split(".")[0:4])
    
    newi["class_id"] = class_id
    newi["family_id"] = family_id
    
    # I only want to split some of the super large families:
    if TFclass[class_id]["label"] in split_class: # classes are too large, split them up
        #if TFfamily[family_id]["label"] in split_family: 
        #    newi["combined_family"] = "%s>%s" % (TFclass[class_id]["label"], TFsubfamily[subfam_id]["label"])
        #    #newi["combined_family"] = "%s>%s>%s" % (TFclass[class_id]["label"], TFfamily[family_id]["label"], TFsubfamily[subfam_id]["label"])
        #else:
        newi["combined_family"] = "%s>%s" % (TFclass[class_id]["label"], TFfamily[family_id]["label"]) 
    else:
        newi["combined_family"] = TFclass[class_id]["label"]
    
    newtab.append(newi)

gl = genelist()
gl.load_list(newtab)
gl.sort("id")
print gl

# get official annotations:
hg19 = glload(os.path.expanduser("~/hg19/hg19_ensembl_v73-ensg-entrez.glb"))
gl = gl.map(genelist=hg19, key="ensg")
gl.saveTSV("TFclass.table.Hs.tsv", key_order=["name", "ensg", "label", "id", "class_id", "combined_family", "family_id"])



