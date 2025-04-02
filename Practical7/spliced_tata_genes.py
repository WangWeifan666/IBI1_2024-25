import re

# Function to process spliced genes and count TATA boxes
def process_spliced_genes(splice_combination, input_file, output_file):
    tata_pattern = r'TATA[AT]A[AT]'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        gene_name = None
        sequence = []
        for line in infile:
            if line.startswith('>'):
                if gene_name and re.search(tata_pattern, ''.join(sequence)):
                    tata_count = len(re.findall(tata_pattern, ''.join(sequence)))
                    outfile.write(f'>{gene_name} TATA_count={tata_count}\n')
                    outfile.write(''.join(sequence))
                gene_name = line.split()[0][1:]  # Extract gene name
                sequence = []
            else:
                sequence.append(line.strip())
        # Check the last gene
        if gene_name and re.search(tata_pattern, ''.join(sequence)):
            tata_count = len(re.findall(tata_pattern, ''.join(sequence)))
            outfile.write(f'>{gene_name} TATA_count={tata_count}\n')
            outfile.write(''.join(sequence))

# Example usage
splice_combination = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ")
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = f'{splice_combination}_spliced_genes.fa'
process_spliced_genes(splice_combination, input_file, output_file)