import matplotlib.pyplot as plt

# Prepare the data
# Regional and population data of the United Kingdom
uk_labels = ['England', 'Wales', 'Northern Ireland', 'Scotland']
uk_pop = [57.11, 3.13, 1.91, 5.45]

# Provinces and Population Data of China
china_labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
china_pop = [65.77, 41.88, 45.28, 61.27, 85.15]

# Sort the data (in ascending order by population)
sorted_uk = sorted(zip(uk_pop, uk_labels), key=lambda x: x[0])
sorted_uk_pop = [pop for pop, _ in sorted_uk]
sorted_uk_labels = [label for _, label in sorted_uk]

sorted_china = sorted(zip(china_pop, china_labels), key=lambda x: x[0])
sorted_china_pop = [pop for pop, _ in sorted_china]
sorted_china_labels = [label for _, label in sorted_china]

# Print the sorted list
print("Sorted UK populations (millions):", sorted_uk_pop)
print("Sorted China neighboring provinces populations (millions):", sorted_china_pop)

# Set icon style
plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Draw a pie chart of the United Kingdom
explode_uk = (0, 0, 0, 0.1)  # Highlight England
colors_uk = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
ax1.pie(
    sorted_uk_pop,
    labels=sorted_uk_labels,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode_uk,
    colors=colors_uk,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5},
    textprops={'fontsize': 10}
)
ax1.set_title('UK Population Distribution', fontsize=14, pad=20)

# Draw a pie chart of China
explode_china = (0, 0, 0, 0, 0.1)  # Highlight Jiangsu
colors_china = ['#FFD700', '#98FB98', '#FFA07A', '#87CEEB', '#DDA0DD']
ax2.pie(
    sorted_china_pop,
    labels=sorted_china_labels,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode_china,
    colors=colors_china,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5},
    textprops={'fontsize': 10}
)
ax2.set_title('Zhejiang Neighboring Provinces Population Distribution', fontsize=14, pad=20)

# Adjust the layout and display
plt.tight_layout()
plt.show()