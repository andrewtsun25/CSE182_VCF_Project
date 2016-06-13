# CSE182_VCF_Project

This repository contains a variety of shell files and python scripts, 
along with their dependencies to run the OMIM pipeline as specified in 
the report. 

Organization:

resources - where all resource files are
resources/vcf_files - where all the chromosomal resource files go
resources/filtered_vcf_files - where all the chromosomal resource files that contain only our individual (52-AA) go.
resources/output_files - where all the output files go. Note that the snpEff_summary.html file generated with our pipeline is placed in shell. 
shell - where all the bash scripts are
src - where all the python scripts are

Overall workflow: 

1. Call shell/get_individual.sh to filter out other individuals in all the chromosomal vcf files. 
2. Aggregate all filtered chromosomal vcfs into a single vcf using shell/aggregate_vcf.sh
3. Liftover the aggregated vcf from hg18 to hg19 coordinates using src/hg18tohg19liftoer.py
4. Annotate lifted over vcf with GRCh37.75 (hg19) annotations using snpeff.
5. (Experimental but not deployed) Filter out vcf for SNP's that have an impact. 
6. Get all the rsID's of the filtered vcf by calling src/vcf_methods.py
7. Translate all rsID's to OMIM Id's, generate a webpage with OMIM entries using src/rsid_to_omim.py


Usage: 

1. Place the chromosomal vcf files of interest in resources/vcf_files. 
2. Run shell/omim_pipeline.sh without any arguments. 
