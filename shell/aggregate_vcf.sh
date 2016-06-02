#!/bin/bash
GFILE='../resources/filtered_vcf_files/complete_genome.vcf'  # File to aggregate all files to
hFILE='header.txt' #File to store the header of the VCF
vFILE='../resources/filtered_vcf_files/filter.CMS_nonCMS_chr1.annotated.phased.vcf' #Get the first vcf file (chr1)
headString="#"    #expected start of every header line

cat ${vFILE} | while read line;
do
   startString=${line:0:1}
   echo "line is: $line"
   echo "start of line is: $startString"
   if [ "$startString" == "$headString" ];
   then
       echo "$line" >> ${hFILE}
   else
       break
   fi
done
cat ${hFILE} >> ${GFILE}  # Put a VCF header onto the new file.
echo "Created $GFILE"echo "Appended VCF header."
for vcf_file in ../resources/filtered_vcf_files/filter.CMS*.vcf;  # Loop over all vcf files.
do
	sed -n '/^#/!p' ${vcf_file} >> ${GFILE}    # Append all lines without '#' character in order they are read to new vcf.
	echo "$vcf_file concatenated to ${GFILE}"
done
echo "[DONE] All vcf files concatenated to single VCF, located at $GFILE"