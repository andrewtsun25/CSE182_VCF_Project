from collections import defaultdict
import re

with open('OmimVarLocusIdSNP.bcp') as linetext:
    line = linetext.readlines()

def rsid_to_omim(line):
    rsid_omim = {}
    omim_temp = ""
    #rsid_temp = ""
    omim_id_regexp = re.compile('[0-9]+')

    for i in line:
        linesplit = i.split('\t')
        rsid = 'rs' + linesplit[len(linesplit)-1][:-1]

        omim_id = linesplit[0]
        is_omim_id = omim_id_regexp.match(omim_id)

        if is_omim_id:
            omim_temp = omim_id

        rsid_omim[rsid] = omim_temp
        omim_temp = ""
        #rsid_temp = ""
    return rsid_omim

convert = rsid_to_omim(line)

for i in convert:
    print (convert[i])

#for i in range (2000):
#    print (line[i])