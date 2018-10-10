"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

from glbase3 import *

mapper = genelist("/Volumes/RAID2/Genomes/hg19/hg19_ensembl_v73-ensg-enst-ensp-name.tsv", 
    format={"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3})
#mapper = glload(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-entrez.glb"))
#print mapper

rbp_form = {"force_tsv": True, "ensp": 1, 'name': 0}

dbd = genelist("RNABPDB_huma_data.txt", format=rbp_form)
dbd = dbd.map(genelist=mapper, key='ensg').removeDuplicates('ensp')
dbd.save('rbp_db_hg38.glb')
dbd.saveTSV('rbp_db_hg38.tsv', key_order=['ensg', 'ensp', 'name'])