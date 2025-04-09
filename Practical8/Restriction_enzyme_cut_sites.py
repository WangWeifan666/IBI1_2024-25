def find_restriction_sites(dna_sequence, enzyme_sequence):
    # Check if sequences contain only valid nucleotides
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    for seq in [dna_sequence, enzyme_sequence]:
        if any(c not in valid_nucleotides for c in seq):
            return ("Error: Sequences must only contain 'A', 'C', 'G', 'T'.")
    
    enzyme_length = len(enzyme_sequence)
    cut_positions = []
    
    # Iterate through possible starting positions
    for i in range(len(dna_sequence) - enzyme_length + 1):
        if dna_sequence[i:i+enzyme_length] == enzyme_sequence:
            cut_positions.append(i)
    
    return cut_positions

# Example
print(find_restriction_sites("GATCGATCGATC", "GATC"))  # Output: [0, 4, 8]
