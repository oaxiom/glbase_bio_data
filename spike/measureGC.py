
from __future__ import division
from glbase import *

ercc = genelist("ERCC92.fa", format=format.fasta)
ercc.sort("name")

newl = []
for f in ercc:
    seq = f["seq"].upper()
    gc = seq.count("C") + seq.count("G")
    gc = gc / len(seq)
    
    newl.append({"name": f["name"], "gc": gc})
    
gl = genelist()
gl.load_list(newl)
gl.saveTSV("ercc_spike_gc_content.txt", key_order=["name", "gc"])