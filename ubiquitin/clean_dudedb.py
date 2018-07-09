
# clean the dud-db data.

from glbase3 import *

def clean_dudedb(filename):
    entry = []
    oh = open(filename, 'rU')
    for line in oh:
        if '#' in line: 
            continue
        if '>' in line:
            t = line.split('|')
            e = {'name': t[2].strip(), 
                'ensg': t[1].strip(),
                'ensp': t[0].strip('>')}
            entry.append(e)
    gl = genelist()
    gl.load_list(entry)
    return(gl)

mm = clean_dudedb('Mm.txt')
mm.save('dudedb-Mm.glb')
mm.saveTSV('dudedb-Mm.tsv', key_order=['ensg', 'ensp', 'name'])

mm = clean_dudedb('Hs.txt')
mm.save('dudedb-Hs.glb')
mm.saveTSV('dudedb-Hs.tsv', key_order=['ensg', 'ensp', 'name'])