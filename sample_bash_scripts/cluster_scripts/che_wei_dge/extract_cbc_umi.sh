#!/usr/bin/env bash

#$ -l h_rt=15:00:00 -l h_vmem=370G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

bc_reads="/fast/AG_Ohler/manuel/che_wei_data/data_2/barcode_umi.fastq"
output="/fast/AG_Ohler/manuel/che_wei_data/data_2"
umi_out_name="extracted_umis"
cbc_out_name="extracted_cbcs"

python3 $scripts/extract_cbc_umi.py \
    --bc_reads $bc_reads \
    --out_dir $output \
    --cbc_out_name $cbc_out_name \
    --umi_out_name $umi_out_name \
    --mode "10X"




