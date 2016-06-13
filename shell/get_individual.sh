#!/usr/bin/env bash
#create directory to store all the filtered vcf files that have only the 52-AA individuals
if [ ! -d ../filtered_vcf_files/ ];
then
    echo "creating new directory"
    mkdir ../filtered_vcf_files/
fi

output_dir='../filtered_vcf_files/'
#loop through each vcf file, use vcf tools to filter out 52-AA sample
for vcf_file in ../vcf_files/CMS*.vcf;
do
    file_string="${vcf_file}"
    vcf_file_name_shortened="${file_string##*/}"
    echo "new shortened name is $vcf_file_name_shortened"
    output_file="${output_dir}filter.${vcf_file_name_shortened}"
    echo "output path is: $output_file"
    vcftools --vcf ${vcf_file} --indv 52-AA --recode --recode-INFO-all  --stdout > $output_file
done
