
import sys, os
from glbase3 import *
user_path = os.path.expanduser("~")
mm10_ensg = glload(os.path.join(user_path, "mm10", "mm10_ensembl_v92_ensg.glb")).getColumns(['name', 'ensg'])
hg38_ensg = glload(os.path.join(user_path, "hg38", "hg38_ensembl_v89-ensg.glb")).getColumns(['name', 'ensg'])

# mouse
form_mouse = {'force_tsv': False, 'name': 9}

epifactors_mm10 = genelist(filename='EpiGenes_main.txt', format=form_mouse).map(genelist=mm10_ensg, key='name')
epifactors_mm10 = epifactors_mm10.removeDuplicates('ensg')
epifactors_mm10.save('mm10_EpiGenes_main.glb')
epifactors_mm10.saveTSV('mm10_EpiGenes_main.tsv', key_order=['ensg', 'name'])

# human
form_human = {'force_tsv': False, 'name': 1}
epifactors_hg38 = genelist(filename='EpiGenes_main.txt', format=form_human).map(genelist=hg38_ensg, key='name')
epifactors_hg38 = epifactors_hg38.removeDuplicates('ensg')
epifactors_hg38.save('hg38_EpiGenes_main.glb')
epifactors_hg38.saveTSV('hg38_EpiGenes_main.tsv', key_order=['ensg', 'name'])

# Make full versions, including more info;

# mouse
form_mouse_full = {'force_tsv': False,
    'name': 9,
    'function': 15,
    'modification': 16,
    'target': 19,
    'specific_target': 20,
    'product': 21,
    'complex': 18}

epifactors_mm10 = genelist(filename='EpiGenes_main.txt', format=form_mouse_full).map(genelist=mm10_ensg, key='name')
epifactors_mm10 = epifactors_mm10.removeDuplicates('ensg')
epifactors_mm10.save('mm10_EpiGenes_full.glb')
epifactors_mm10.saveTSV('mm10_EpiGenes_full.tsv', key_order=['ensg', 'name'])

# mouse
form_human_full = {'force_tsv': False,
    'name': 1,
    'function': 15,
    'modification': 16,
    'target': 19,
    'specific_target': 20,
    'product': 21,
    'complex': 18}

epifactors_hg38 = genelist(filename='EpiGenes_main.txt', format=form_human_full).map(genelist=hg38_ensg, key='name')
epifactors_hg38 = epifactors_hg38.removeDuplicates('ensg')
epifactors_hg38.save('hg38_EpiGenes_full.glb')
epifactors_hg38.saveTSV('hg38_EpiGenes_full.tsv', key_order=['ensg', 'name'])
