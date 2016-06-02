#!/usr/bin/env bash
#get the complete genome file
vcfDir='../resources/filtered_vcf_files/'
vFile="${vcfDir}complete_genome.vcf"
echo "vFile name is: ${vFile}"

tempFile="${vcfDir}complete_genome_hg19.vcf"
echo "tempFile name is: ${tempFile}"


#if the hg19 file already exists, remove it to avoid writing over
if [ -f ${tempFile} ];
then
    echo "removing tempFile (hg19 file)"
    rm ${tempFile}
fi

#python executable path
pythonExe='/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4'

echo "about to run liftover script"
#liftover to hg19
${pythonExe} ../src/hg18tohg19liftover.py -i ${vFile}

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
filter_text="((EFF[*].IMPACT = 'HIGH' ) | (EFF[*].IMPACT = 'MODERATE' )) & (QUAL >= 20) & (EFF[*].EFFECT != 'SYNONYMOUS_CODING' ) & ((EFF[*].FUNCLASS = 'MISSENSE' ) | (EFF[*].FUNCLASS) = 'NONSENSE' ) rmRefGen"
echo "filter_text is ${filter_text}"



echo "running snpsift command"
snpeff eff -v GRCh37.75 ${inputFile} > ${annotatedFile}
snpsift filter ${filter_text} ${annotatedFile} > ${filteredFile}
echo "done running snpsift"

#get all the rsIDs from the new filtered vcf file
${pythonExe} ../src/vcf_methods.py ${filteredFile}


