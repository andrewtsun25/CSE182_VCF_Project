from vcf_conf import defaultConfig

vcf_reader = defaultConfig.read_vcf()

# INFO=<ID=AF,Number=A,Type=Float,Description="Estimated Allele Frequencies">
# INFO=<ID=AR2,Number=1,Type=Float,Description="Allelic R-Squared: estimated correlation between most probable ALT dose and true ALT dose">
# INFO=<ID=DR2,Number=1,Type=Float,Description="Dosage R-Squared: estimated correlation between estimated ALT dose [P(RA) + 2*P(AA)] and true ALT dose">
# FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
# FORMAT=<ID=DS,Number=1,Type=Float,Description="estimated ALT dose [P(RA) + P(AA)]">
# FORMAT=<ID=GP,Number=G,Type=Float,Description="Estimated Genotype Probability">

for i, record in enumerate(vcf_reader):
    # Information extraction
    alt = record.ALT
    chrom = record.CHROM
    fmt = record.FORMAT
    rsid = record.ID
    af = record.INFO['AF']
    ar2 = record.INFO['AR2']
    dr2 = record.INFO['DR2']
    pos = record.POS
    ref = record.REF

    # Sample-specific extraction
    call = record.sample[7]
    print('Record #{}: {}'.format(i, record))
