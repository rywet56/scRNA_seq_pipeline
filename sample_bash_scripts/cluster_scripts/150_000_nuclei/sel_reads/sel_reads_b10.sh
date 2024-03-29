#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=450G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

path_to_cbcs_sam="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/aligned_cbs/aligned_cbcs_b10.sam"

path_to_bc_comb="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/barcode_combinations.fasta"

path_to_umis_fastq="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/extracted_cbcs_umis/extracted_umis_b10.fastq"

path_to_gen_fastq="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/batch_10/SRR6750051_1.fastq"

out_dir="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/sel_reads"

out_filename_bcs="selected_barcodes_b10"
out_filename_umis="selected_umis_b10"
out_filename_gen="selected_gens_b10"

python3 $scripts/select_bcs_umis_genes.py \
     --sam_in $path_to_cbcs_sam \
     --cbc_comb $path_to_bc_comb \
     --umi_in $path_to_umis_fastq \
     --gen_reads $path_to_gen_fastq \
     --out_dir $out_dir \
     --cbc_out_name $out_filename_bcs \
     --umi_out_name $out_filename_umis \
     --gene_out_name $out_filename_gen
     
