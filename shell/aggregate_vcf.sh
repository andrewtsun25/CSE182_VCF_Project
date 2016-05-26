#!/bin/bash
GFILE='complete_genome.vcf'  # File to aggregate all files to
cat header.txt > $GFILE  # Put a VCF header onto the new file.
echo "Created $GFILE"
echo "Appended VCF header."
for vcf_file in CMS*.vcf;  # Loop over all vcf files.
do
	sed -n '/^#/!p' $vcf_file >> $GFILE    # Append all lines without '#' character in order they are read to new vcf.
	echo "$vcf_file concatenated to $GFILE"
done
echo "[DONE] All vcf files concatenated to single VCF, located at $GFILE"