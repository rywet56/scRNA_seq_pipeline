#!/usr/bin/env bash

#$ -l h_rt=01:00:00 -l h_vmem=10G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

clusters="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/cal_clu_10.txt"
out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei"

name="dge_matrix_umid0"

python3 $scripts/calculate_DGE_matrix.py \
    --clusters $clusters \
    --out_dir $out \
    --file_name $name
