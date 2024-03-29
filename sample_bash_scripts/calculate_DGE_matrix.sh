#!/usr/bin/env bash

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"


#clusters="/Users/manuel/Desktop/cluster_out.txt"
#out="/Users/manuel/Desktop"

clusters="/Users/manuel/Desktop/bowtie_strategy/cluster_out.txt"
out="/Users/manuel/Desktop/bowtie_strategy"

name="expression"

python3 $scripts/calculate_DGE_matrix.py \
    --clusters $clusters \
    --out_dir $out \
    --file_name $name
