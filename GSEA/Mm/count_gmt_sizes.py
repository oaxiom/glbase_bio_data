

import sys, os, glob, statistics

for f in glob.glob('*/*.gmt'):
    bn = os.path.split(f)[1].replace('.gmt', '')

    oh = open(f, 'rt')
    lengths = []
    for line in oh:
        l = line.strip().split('\t')[2:]
        lengths.append(len(l))

    oh.close()

    vmin = min(lengths)
    vmax = max(lengths)
    vmean = statistics.mean(lengths)
    vstd = statistics.stdev(lengths)
    print(f'{f}:\n\t\tmin={vmin}\tmean={vmean:.1f}\tmax={vmax}\tstd={vstd:.1f}')
