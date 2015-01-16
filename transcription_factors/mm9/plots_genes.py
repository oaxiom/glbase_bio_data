

import matplotlib.cm as cm
from glbase import *
config.draw_mode = "png"

arr = glload("../rsem-genes/genes_cpm_expression.glb")
tfs = glload("all_tfs.glb").removeDuplicates("name")

arr.log(2)
tree = arr.tree(filename="tree.png", row_names=arr["name"], color_threshold=0.0)
arr.unlog(2)

genes = tfs["name"]
    
for g in genes:
    if g: # occasional blanks
        arr.barh_single_item(value=g, key="name", filename="plots/barh_%s.png" % g, 
            tree=tree, yticklabel_fontsize=7, size=(6,16))

