# File paths
human_file = r"IBI1_2024-25\\Practical 13\\P04179.fasta.txt"
mouse_file = r"IBI1_2024-25\\Practical 13\\P09671.fasta.txt"
random_file = r"IBI1_2024-25\\Practical 13\\random.fasta.txt"
blosum_file = r"IBI1_2024-25\\Practical 13\\BLOSUM62.txt"

# Read sequences
human_seq = ''.join([line.strip() for line in open(human_file) if not line.startswith('>')])
mouse_seq = ''.join([line.strip() for line in open(mouse_file) if not line.startswith('>')])
random_seq = ''.join([line.strip() for line in open(random_file) if not line.startswith('>')])

# Load BLOSUM62 matrix
blosum_matrix = {}
with open(blosum_file) as f:
    lines = [line for line in f if line.strip() and not line.startswith('#')]
    columns = lines[0].split()
    for row in lines[1:]:
        parts = row.split()
        amino_acid = parts[0]
        for col, score in zip(columns, parts[1:]):
            blosum_matrix[(amino_acid, col)] = int(score)

# Calculate similarity and scores
human_mouse_sim = sum(1 for a, b in zip(human_seq, mouse_seq) if a == b) / len(human_seq)
human_random_sim = sum(1 for a, b in zip(human_seq, random_seq) if a == b) / len(human_seq)
mouse_random_sim = sum(1 for a, b in zip(mouse_seq, random_seq) if a == b) / len(mouse_seq)

human_mouse_score = sum(blosum_matrix[(a, b)] for a, b in zip(human_seq, mouse_seq))
human_random_score = sum(blosum_matrix[(a, b)] for a, b in zip(human_seq, random_seq))
mouse_random_score = sum(blosum_matrix[(a, b)] for a, b in zip(mouse_seq, random_seq))

# Print results with precise formatting
print(f"Human-Mouse Similarity: {human_mouse_sim * 100:.2f}%")
print(f"Human-Mouse Score: {human_mouse_score}")
print(f"Human-Random Similarity: {human_random_sim * 100:.2f}%")
print(f"Human-Random Score: {human_random_score}")
print(f"Mouse-Random Similarity: {mouse_random_sim * 100:.2f}%")
print(f"Mouse-Random Score: {mouse_random_score}")
print(f"SOD2 Length: {len(human_seq)}")
            
    
