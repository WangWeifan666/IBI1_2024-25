# Define the gene sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
# Define the splice-donor dinucleotide
donor = 'GT'
# Define the splice-acceptor dinucleotide
acceptor = 'AG'
# Initialize the maximum intron length
max_length = 0

# Iterate through the sequence to find splice-donor sites
for i in range(len(seq)):
    if seq[i:i+2] == donor:
        # Iterate through the sequence after the splice-donor site to find splice-acceptor sites
        for j in range(i+2, len(seq)):
            if seq[j:j+2] == acceptor:
                # Calculate the length of the intron
                intron_length = j - i + 2
                # Update the maximum intron length if the current intron is longer
                if intron_length > max_length:
                    max_length = intron_length

# Print the length of the largest possible intron
print(f"The length of the largest possible intron is: {max_length}")
    