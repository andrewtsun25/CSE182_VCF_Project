import re
import webbrowser
import sys
import os

# Creates a dictionary from OmimVarLocusIdSNP of rsid -> OMIM number
def rsid_to_omim():
    rsid_omim = {}
    # Checks to see if the OMIM is a regular expression
    omim_id_regexp = re.compile('[0-9]+')

    #  Opens OmimVarLocusIdSNP and reads through it, creating the dictionary
    for i in open('../resources/OmimVarLocusIdSNP.bcp'):
        linesplit = i.split('\t')
        rsid = 'rs' + linesplit[len(linesplit)-1][:-1]
        omim_id = linesplit[0]
        rsid_omim[rsid] = omim_id if omim_id_regexp.match(omim_id) else ''
    return rsid_omim

# Create a URL for the OMIM API from a list of rsids
def generate_url(args, mode='entry', openURL=False):
    rsid_to_omim_dict = rsid_to_omim()
    unique_omims = set(rsid_to_omim_dict[rsid] for i, rsid in enumerate(args) if rsid in rsid_to_omim_dict)

    # Changes type of search according to the input
    base_url = "http://api.omim.org/api/clinicalSynopsis?" if mode == 'clinical_significance' else "http://api.omim.org/api/entry?"
    query_str = ''

    # Eliminates duplicates
    for omim in unique_omims:
        query_str += ("&mimNumber=" + omim)
    query_str = query_str[1:]

    # Concatanates the queries in the URL
    query_str += "&format=html" if query_str else 'format=html'
    url = base_url + query_str

    msg = 'Clinical Significance Results from OMIM: {}'.format(url) if mode == 'clinical_significance' \
        else 'Entries from OMIM: {}'.format(url)
    print(msg)

    # Opens up URL in web browser
    if openURL:
        webbrowser.open(url)

if __name__ == '__main__':
    rsids = open(sys.argv[1], 'r')
    rsids_list = [rsid.strip() for rsid in rsids]
    generate_url(rsids_list)