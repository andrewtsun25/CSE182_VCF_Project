import re
import webbrowser
import sys


def rsid_to_omim():
    rsid_omim = {}
    omim_id_regexp = re.compile('[0-9]+')

    for i in open('OmimVarLocusIdSNP.bcp'):
        linesplit = i.split('\t')
        rsid = 'rs' + linesplit[len(linesplit)-1][:-1]
        omim_id = linesplit[0]
        rsid_omim[rsid] = omim_id if omim_id_regexp.match(omim_id) else ''
    return rsid_omim


def generate_url(args, mode='entry', openURL=True):
    rsid_to_omim_dict = rsid_to_omim()
    unique_omims = set(rsid_to_omim_dict[rsid] for i, rsid in enumerate(args) if rsid in rsid_to_omim_dict and i >= 1)
    base_url = "http://api.omim.org/api/clinicalSynopsis?" if mode == 'clinical_significance' else "http://api.omim.org/api/entry?"
    query_str = ''
    for omim in unique_omims:
        query_str += ("&mimNumber=" + omim)
    query_str = query_str[1:]
    query_str += "&format=html" if query_str else 'format=html'
    url = base_url + query_str
    msg = 'Clinical Significance Results from OMIM: {}'.format(url) if mode == 'clinical_significance' \
        else 'Entries from OMIM: {}'.format(url)
    print(msg)
    if openURL:
        webbrowser.open(url)

if __name__ == '__main__':
    generate_url(sys.argv)