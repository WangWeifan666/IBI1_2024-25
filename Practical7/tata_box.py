import re

def extract_gene_name(header):
    # Extract the gene name from the header line (assuming the format is gene:GENENAME)
    match = re.search(r'gene:([\w-]+)', header)
    return match.group(1) if match else None

def main():
    tata_pattern = re.compile(r'TATA[AT]A[AT]')  # TATAWAW pattern
    output = []

    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile:
        current_gene, current_seq = None, []
        for line in infile:
            if line.startswith('>'):
                # Process the previous gene
                if current_gene:
                    seq = ''.join(current_seq)
                    if tata_pattern.search(seq):
                        # Format the sequence with 60 characters per line
                        formatted_seq = '\n'.join(seq[i:i+60] for i in range(0, len(seq), 60))
                        output.append(f'>{gene_name}\n{formatted_seq}\n')
                # Extract the new gene name
                current_gene = line.strip()
                gene_name = extract_gene_name(current_gene)
                current_seq = []
            else:
                current_seq.append(line.strip())
        # Process the last gene
        if current_gene:
            seq = ''.join(current_seq)
            if tata_pattern.search(seq):
                formatted_seq = '\n'.join(seq[i:i+60] for i in range(0, len(seq), 60))
                output.append(f'>{gene_name}\n{formatted_seq}\n')

    with open('tata_genes.fa', 'w') as outfile:
        outfile.writelines(output)

if __name__ == "__main__":
    main()