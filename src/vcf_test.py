import vcf

vcf_path = '../resources/chrom1.vcf'
test_vcf = vcf.Reader(vcf_path, 'w')
for i, record in enumerate(vcf_path)
    print('Record #{}: {}'.format(i, record))