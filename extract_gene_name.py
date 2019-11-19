# This script is used to  extract the gene name for every read from a sam file
# and saves it in a txt file in queryname order.
from tools.file_input_output import read_from_file
from tools.sam_tools import bubble_sort, sort_sam_built_in
from tools.utils import get_cmd_args, get_resources_used


@get_resources_used
def write_gene_names_to_file(path_to_sam, out_dir, file_name):
    read_list = read_from_file(file_type="sam", input_file=path_to_sam)

    sorted_sam = sort_sam_built_in(read_list)

    output = out_dir + "/" + file_name
    handler = open(output + ".txt", "w")


# some gn tags have two genes. intronic mappings can be ignored
    unique_mappings = 0
    not_unique = 0
    no_mapping = 0
    for entry in sorted_sam:
        if entry.has_tag('gn'):  # did this read align anywhere in the genome?
            gene_names = entry.get_tag('gn').split(',')
            if len(gene_names) < 2:
                unique_mappings += 1
                handler.write(entry.get_tag('gn'))
            else:
                not_unique += 1
                handler.write('no_gene')
        else:
            no_mapping += 1
            handler.write('no_gene')

        handler.write("\n")

#     for entry in sorted_sam:
#         if entry.has_tag('gn'):
#             handler.write(entry.get_tag('gn'))
#         else:
#            handler.write('no_gene')
#         handler.write("\n")

    handler.close()
    print("unique mappings: " + str(unique_mappings))
    print("not unique mappings: " + str(not_unique))
    print("no mapping: " + str(no_mapping))


def main(cmd_args):
    path_to_sam = cmd_args['sam_in']
    outdir = cmd_args['out_dir']
    filename = cmd_args['file_name']

    write_gene_names_to_file(path_to_sam=path_to_sam, out_dir=outdir, file_name=filename)


if __name__ == "__main__":
    main(get_cmd_args())
