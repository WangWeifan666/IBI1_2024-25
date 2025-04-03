import re

valid_combinations = {"GTAG", "GCAG", "ATAC"}
spiked_combination = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()
while spiked_combination not in valid_combinations:
    print("Invalid input! Please choose from GTAG, GCAG, ATAC.")
    spiked_combination = input("Enter combination: ").strip().upper()
# Process the spliced genes
# Expression for TATA box pattern
tata_pattern = r"TATA[AT]A[AT]"
input_path = r"C:\Users\ASUS\Desktop\Github\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_filename = fr"C:\Users\ASUS\Desktop\Github\IBI1_2024-25\Practical7\{spiked_combination}_spliced_genes.fa"
# Sequence Processing
with open(input_path, 'r') as infile, open(output_filename,'w') as outfile:
    gene_name = None #Track current gene name
    sequence = []
    for line in infile:
        if line.startswith('>'):
            if gene_name and re.search(tata_pattern, ''.join(sequence)):
                if re.search(fr'{spiked_combination}',''.join(sequence)):
                    tata_count = len(re.findall(tata_pattern, ''.join(sequence)))
                    outfile.write(f'>{gene_name} TATA_count={tata_count}\n')
                    outfile.write(''.join(sequence) + '\n')
            gene_name = line.split()[3][5:]  # Extract gene name
            sequence = []
        else:
            sequence.append(line.strip())
    # Check the last gene
    if gene_name and re.search(tata_pattern, ''.join(sequence)):
       if re.search(fr'{spiked_combination}',''.join(sequence)):
            tata_count = len(re.findall(tata_pattern, ''.join(sequence)))
            outfile.write(f'>{gene_name} TATA_count={tata_count}\n')
            outfile.write(''.join(sequence) + '\n')