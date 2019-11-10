"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

from glbase3 import *

mapper = genelist(os.path.expanduser("~/hg38/hg38_ensg_enst_ensp_name_v94.txt"), 
    format={"force_tsv": True, "ensg": 0, 'enst': 1, "ensp": 2, "name": 3})
#mapper = glload(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-entrez.glb"))
print(mapper)

rbp_form = {"force_tsv": True, "ensg": 1, 'name': 0}

dbd = genelist("RNABPDB_huma_data.txt", format=rbp_form)
dbd = dbd.map(genelist=mapper, key='ensg').removeDuplicates('ensg')
dbd.save('rbp_db_hg38.glb')
dbd.saveTSV('rbp_db_hg38.tsv', key_order=['ensg', 'enst', 'ensp', 'name'])