from vcf_config import andrew_config

vcf_reader = andrew_config.read_vcf()

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
    af = record.INFO['AF']  # Estimated allele frequencies
    ar2 = record.INFO['AR2']  # Allelic R-Squared
    dr2 = record.INFO['DR2']  # Dosage R-Squared
    pos = record.POS
    ref = record.REF

    # Patient-specific extraction
    call = record.samples[7]
    patient_id = call.sample  # Patient referenced by ID
    gt = call.data.GT  # Genotype
    ds = call.data.DS  # Estimated ALT dose
    gp = call.data.GP  # Estimated Genotype Probability
    print('Record #{}: {}'.format(i, record))
