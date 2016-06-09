import time
import sys
import vcf


def sort_rsids(vcf_reader):
    '''
     This function loops through the vcf file, and outputs a list of homozyous alt and hetereozygous
     variants from the vcf file.
    :param vcf_reader: This is a vcf Reader object that will allow us to parse through the vcf file
    :return: list of rsids for homozygous alt variants and heterozygous variants.
    '''
    hom_ids = []
    het_ids = []

    #loop through the vcf file
    for record in vcf_reader:
        rsID = record.ID     #get the rsID

        for call in record:
            #only get the rsIDs of varaints
            if call.is_variant:
                if call.gt_type == 1:
                    het_ids.append(rsID)
                elif call.gt_type == 2:
                    hom_ids.append(rsID)

    return hom_ids, het_ids         #return list of rsIDs for homozygous alt and heterozygous alt


def main(argv):
    start_time = time.time()
    print("argv is: " + str(argv))
    input_file = argv[1]
    vcf_reader = vcf.Reader(open(str(input_file),'r'))

    homo_ids, het_ids = sort_rsids(vcf_reader)
    print("number of homozygous variants are: " + str(len(homo_ids)))
    print("number of heterozygous variants are: " + str(len(het_ids)))

    with open("../resources/output_files/outputHom.txt", "w") as outputHom, \
            open("../resources/output_files/outputHet.txt", "w") as outputHet:
            for rsID in homo_ids:
                outputHom.write(str(rsID) + "\n")
            for rsID in het_ids:
                outputHet.write(str(rsID) + "\n")

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == '__main__':
    main(sys.argv)

