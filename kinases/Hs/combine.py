"""

Merge TF DBD and GO category into a single file containing ENSG and name

"""

from glbase3 import *

mapper = genelist("/Volumes/RAID2/Genomes/hg19/hg19_ensembl_v73-ensg-enst-ensp-name.tsv", 
    format={"force_tsv": True, "ensg": 0, "enst": 1, "ensp": 2, "name": 3})
#mapper = glload(os.path.join(os.path.expanduser("~"), "hg19/hg19_ensembl_v73-ensg-entrez.glb"))
#print mapper

kin_form = {"force_tsv": True, 'name': 23}

dbd = genelist("Kincat_Hsap.08.02.txt", format=kin_form)
dbd = dbd.map(genelist=mapper, key='name').removeDuplicates('ensg')
dbd.save('kinome_db.glb')
dbd.saveTSV('kinome_db.tsv', key_order=['ensg', 'ensp', 'name'])