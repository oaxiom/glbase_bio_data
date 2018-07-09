

# Clean-up the TFCat data. 
# I want to delet the first two columns, but don't want to put it into excal as it mangles the names

awk -F"\t" '{printf "%s\t%s\t%s\t%s\n", $3,$4,$5,$6}' TFCat-TFGene.tsv >TFCat_table.cleaned.tsv


