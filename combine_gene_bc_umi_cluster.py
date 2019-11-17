from tools.file_input_output import read_from_file
from tools.utils import get_resources_used


def get_gene_name(genes, read_id):
    '''
    the read_id has nothing to do with the query_name in the fastq file
    :param read_id: an integer that specifies the line number of a read
    :return: a gene name as a string
    '''
    return genes[int(read_id)-1]


def get_umi_number(read_umi_list, read_number):
    return read_umi_list[int(read_number)-1]


def get_read_umi_list(umis, number_of_reads):
    '''
    Returns a list that maps umi_cluster number to read_number
    :param umis: a list that contains clustering results of UMI's. Every list entry corresponds to one cluster.
                [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param number_of_reads:
    :return: {read_number:umi_cluster_number, ...}
    The first read has index 0 (not 1)
    '''
    read_umi_list = [0]*number_of_reads
    for cluster_number in range(len(umis)):  # go through all umi clusters
        read_numbers = umis[cluster_number].split("\t")[2].split(",")  # read_numbers = line numbers
        for read_number in read_numbers:
            read_umi_list[int(read_number)-1] = cluster_number+1
    return read_umi_list


def get_number_of_reads(gene_list):
    return len(gene_list)


@get_resources_used
def construct_cluster_umi_file(barcodes, umis, genes, out_dir, file_name):
    '''
    Combines the information of CBC and UMI clustering with gene names from alignment of
    genomic reads into one file that can be used to construct a DGE matrix in another step.
    :param barcodes: [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param umis: [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param genes: [gene_1, gene_2, gene45, ... ]
    '''
    handler = open(out_dir + "/" + file_name + ".txt", "w")
    no_reads = get_number_of_reads(genes)
    read_umi_list = get_read_umi_list(umis, no_reads)

    for cluster in barcodes:
        clust = cluster.split("\t")
        cluster_name = clust[0]
        cluster_size = clust[1]
        handler.write(cluster_name + "\t" + str(cluster_size) + "\t")

        read_numbers = clust[2].split(",")
        no_reads = len(read_numbers)

        for read in range(no_reads):
            read_no = int(read_numbers[read])
            handler.write(get_gene_name(genes, read_no) + ',' + str(get_umi_number(read_umi_list, read_no)))

            if read < no_reads-1:
                handler.write("-")
        handler.write("\n")


path_to_barcodes = "/Users/manuel/Desktop/clustered_barcodes.txt"
path_to_umis = "/Users/manuel/Desktop/clustered_UMIs.txt"
path_to_genes = "/Users/manuel/Desktop/sorted.txt"
path_to_out = "/Users/manuel/Desktop"

barcodes = read_from_file(input_file=path_to_barcodes, file_type="txt")
umis = read_from_file(input_file=path_to_umis, file_type="txt")
genes = read_from_file(input_file=path_to_genes, file_type="txt")

artifical_gene_list = [""]*1000000

for i in range(1000000):
    artifical_gene_list[i] = "gene_" + str(i)

construct_cluster_umi_file(barcodes, umis, artifical_gene_list, out_dir=path_to_out, file_name="cluster_out")

