import time
import sys
import vcf


def sort_rsids(vcf_reader):
    hom_ids = []
    het_ids = []
    for record in vcf_reader:
        rsID = record.ID
        for call in record:
            if call.is_variant:
                if call.gt_type == 1:
                    het_ids.append(rsID)
                elif call.gt_type == 2:
                    hom_ids.append(rsID)
    return hom_ids, het_ids


def main(argv):
    vcf_reader = vcf.Reader(open(argv[0],"r"))
    start_time = time.time()
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

