
# Part 1: Create the dictionary
lang_data = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5
}
print("(1) Dictionary created:")
print(lang_data)

# Part 2: Generate the bar plot
import matplotlib.pyplot as plt

# Extract data for plotting
languages = list(lang_data.keys())
percentages = list(lang_data.values())

# Create bar plot with custom style
plt.figure(figsize=(10, 6))
plt.bar(languages, percentages, color='skyblue', edgecolor='black')

# Customize plot
plt.title('Programming Language Popularity (February 2024)', fontsize=14)
plt.xlabel('Programming Languages', fontsize=12)
plt.ylabel('Percentage of Developers (%)', fontsize=12)
plt.ylim(0, 70)  # Set y-axis limit for better visualization
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for i, percent in enumerate(percentages):
    plt.text(i, percent + 1, f'{percent}%', ha='center')

plt.xticks(rotation=45, ha='right')  # Rotate x-labels for readability
plt.tight_layout()  # Adjust layout

print("\n(2) Bar plot generated. Displaying...")
plt.show()

# Part 3: Retrieve percentage for a specific language
# --- MODIFY THIS VARIABLE TO TEST DIFFERENT LANGUAGES ---
selected_language = 'Python'  # <-- Change this value as needed
# -------------------------------------------------------

percentage = lang_data.get(selected_language, None)
if percentage is not None:
    print(f"\n(3) Percentage of developers using {selected_language}: {percentage}%")
else:
    print(f"\n(3) Language '{selected_language}' not found in the data")