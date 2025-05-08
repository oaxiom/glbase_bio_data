"""

Data is already Hs, so just save

"""

import glob, sys, os
from glbase3 import genelist

ferrdb_format = {'name': 2, 'ensg': 4}
ferrdb_format_small_mol = {'name': 2, 'full_name': 3}

gmt = {}

for filename in glob.glob('FerrDB-20241210/*.csv.gz'):
    name = os.path.split(filename)[1].replace('.csv.gz', '')

    if 'inducer' in filename or 'inhibitor' in filename:
        gl = genelist(filename=filename, name=name, gzip=True, format=ferrdb_format_small_mol)
    else:
        gl = genelist(filename=filename, name=name, gzip=True, format=ferrdb_format)
        gl = gl.removeDuplicates('ensg')

        gmt[name] = gl['name']



    print(gl)

    gl.save(f'{name}.glb')

oh = open('../../GSEA/Hs/cell_death/ferroptosis.gmt', 'wt')

for k in gmt:
    oh.write(f'{k}\t{k}\t')
    genes = '\t'.join(gmt[k])
    oh.write(genes)
    oh.write('\n')
