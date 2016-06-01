from collections import defaultdict
import csv
import sys


def main(argv):
    # Read from igsr file by row.
    if len(argv) != 1:
        print('Usage: {} <input_file>'.format(argv[0]))
    igsr_samples = open(argv[0], 'r')
    igsr_reader = csv.DictReader(igsr_samples, delimiter='\t')
    populations = defaultdict(list)
    # Separate all sample ID's by population
    for index, row in enumerate(igsr_reader):
        population_code = row['Population Code']  # get population
        sample_name = row['Sample name'] # get sample name
        populations[population_code].append(sample_name)
    # Write each population's sample ID's to a list for each population.
    for population, sample_names in populations.items():
        altered_population_code = '_'.join(population.split(' '))  # fix population name to be 'single word'
        out_file = open('{}.txt'.format(altered_population_code), 'w')  # output all members of a population to 1 file
        for sample_name in sample_names:  # output all members of population, each to its own line
            out_file.write(sample_name + '\n')

if __name__ == '__main__':
    main(sys.argv)