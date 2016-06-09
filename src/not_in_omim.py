from rsid_to_omim import rsid_to_omim
from vcf_methods import *
import vcf
import sys

def get_ids_not_omim(omim_dict, vcf_reader):
    '''
    Extra credit function that is able to go through our annoated vcf file,
    identify all the RSids that are not present in OMIM, and outputs the functions
    of these variants.
    :param omim_dict: This is a dictionary mapping the variant OMIM Ids to their respetive rsIDs
    :param vcf_reader: vcf reader object to the annotated input vcf file
    :return: a list of tuples including rsID and annotated info
    '''
    #list of all the annotated rsid tuples in the human
    rsids_annotated_in_vcf = list((record.ID, record.INFO) for record in vcf_reader)
    rsids_in_vcf = set(rsid for rsid, _ in rsids_annotated_in_vcf)
    #list of all rsIDs in omim dictionary
    rsids_in_omim = set(rsid for rsid in omim_dict)
    #get list of all rsIDs in our vcf but not in omim
    rsids_not_in_omim = rsids_in_vcf - rsids_in_omim
    #return rsid and info tuple list
    return [(rsid, info) for rsid, info in rsids_annotated_in_vcf if rsid in rsids_not_in_omim]










def main(argv):
    outputFile = open('../resources/output_files/rsids_not_in_omim.txt','w')
    #pass in the annotated vcf complete genome file (resources/filtered_vcf_files/complete_genome_hg19.vcf.annotated.vcf)
    inputFile = argv[1]

    vcf_reader = vcf.Reader(open(str(inputFile),'r'))
    omim_dict = rsid_to_omim()

    rsid_list = get_ids_not_omim(omim_dict, vcf_reader)
    print("number of rsIDs not in OMIM is: " + str(len(rsid_list)))
    for rsid, info in rsid_list:
        outputFile.write("{}\t{}\n".format(rsid, info))



if __name__ == '__main__': main(sys.argv)