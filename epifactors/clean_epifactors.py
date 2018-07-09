

from glbase import *
user_path = os.path.expanduser("~")
ensg = glload(os.path.join(user_path, "mm10", "mm10_ensembl_v79_ensg.glb")).getColumns(['name', 'ensg'])

# mouse
form_mouse = {'force_tsv': False, 'name': 9}

epifactors_mm10 = genelist(filename='EpiGenes_main.csv', format=form_mouse).map(genelist=ensg, key='name')
epifactors_mm10 = epifactors_mm10.removeDuplicates('ensg')
epifactors_mm10.save('mm10_EpiGenes_main.glb')
epifactors_mm10.saveTSV('mm10_EpiGenes_main.tsv', key_order=['ensg', 'name'])

epifactors_hg38 = genelist(filename='EpiGenes_main.csv', format=form)
