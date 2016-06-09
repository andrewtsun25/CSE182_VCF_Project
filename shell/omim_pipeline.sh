#!/usr/bin/env bash

#if we have not filtered out the 52-AA individual, call script to get individual in each file
if [ ! -d ../filtered_vcf_files/ ];
then
    ./get_individual.sh
fi

#if we haven't yet aggregate the vcf files, aggregate files into complete genome.
if [ ! -f ../resources/filtered_vcf_files/complete_genome.vcf ];
then
    ./aggregate_vcf.sh
fi

#get the complete genome file
vcfDir='../resources/filtered_vcf_files/'
vFile="${vcfDir}complete_genome.vcf"
echo "vFile name is: ${vFile}"

#python executable path
pythonExe='/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4'

#if we have not lifted over to hg19, call liftover script.
if [ ! -f ../resources/filtered_vcf_files/complete_genome_hg19.vcf ];
then
    echo "about to run liftover script"
    #liftover script call
    ${pythonExe} ../src/hg18tohg19liftover.py -i ${vFile}
fi

#get new hg19 vcf file as the new input file for snpeff
inputFile="${vcfDir}complete_genome_hg19.vcf"
echo "inputFile name is: ${inputFile}"


#get an html page of all the statistics
echo "generating html for genome statistics"
snpeff eff -stats hg19 ${inputFile}
echo "done with html file production"

#file that will contain the filtered annotated file
annotatedFile="${inputFile}.annotated.vcf"
filteredFile="${inputFile}.filtered.vcf"

echo "annotatedFile name is: ${annotatedFile}"


#get the statistics of our vcf file in html format
#filter_text="((ANN[*].IMPACT = HIGH) | (ANN[*].IMPACT = MODERATE)) & (QUAL >= 20 ) & (ANN[*].EFFECT != synonymous_variant)"
#
# echo "filter_text is ${filter_text}"


if [ ! -f ${annotatedFile} ];
then
    echo "running snpsift command"
    snpeff eff -v GRCh37.75 ${inputFile} > ${annotatedFile}
fi

#if [ ! -f ${filteredFile} ];
#then
#    snpsift filter ${filter_text} ${annotatedFile} > ${filteredFile}
#    echo "done running snpsift"
#fi
#get all the rsIDs from the new filtered vcf file
${pythonExe} ../src/vcf_methods.py ${annotatedFile}

outDir='../resources/output_files/'

for outputFile in outDir;
do
    ${pythonExe} ../src/rsid_to_omim.py ${outputFile}
done