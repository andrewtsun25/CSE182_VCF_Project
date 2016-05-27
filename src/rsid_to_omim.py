from collections import defaultdict
import re

with open('snp_result.txt') as linetext:
    line = linetext.readlines()

rsid_to_omim_dicts = []
rsid_omim = {}
omim_temp = []
rsid_temp = ""
omim_id_regexp = re.compile('[0-9]+')

for i in line:
    linesplit = i.split('|')
    if linesplit[0][:2] == 'rs':
        #print (i)
        #rsid_omim["rsid"] = linesplit[0]
        rsid = linesplit[0][:-1]

    if len(linesplit) > 2 and linesplit[1] == ' OMIM-CURATED-RECORDS ':
        #print (i)
        #rsid_omim["omim"] = linesplit[0]
        omim_id = linesplit[2][1:-1]
        is_omim_id = omim_id_regexp.match(omim_id)
        if is_omim_id:
            omim_temp.append(omim_id)

    #print (rsid_omim)

    if linesplit[0] == '\n' and omim_temp:
        rsid_omim[rsid] = omim_temp
        rsid_to_omim_dicts.append(rsid_omim)
        rsid_omim = {}
        omim_temp = []
        rsid_temp = ""

for i in rsid_to_omim_dicts:
    print (i)