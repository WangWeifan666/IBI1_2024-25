import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory 
os.chdir("IBI1_2024-25\Practical 10")

# Verify current directory
print("Current working directory:", os.getcwd())
print("Directory contents:", os.listdir())

# Load dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Display first 5 rows
print("\nFirst 5 rows of data:")
print(dalys_data.head(5))

# Show dataset info
print("\nDataset information:")
print(dalys_data.info())

# Show statistical summary
print("\nStatistical summary:")
print(dalys_data.describe())

# Extract Year column (3rd column) for first 10 rows
years_first_10 = dalys_data.iloc[0:10, 2]  # Column index 2 for 'Year'
print("\nYear data for first 10 entries:")
print(years_first_10)
# Answer: 10th year with DALYs data in Afghanistan is 1999

# Filter 1990 data using Boolean indexing
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nDALYs for all countries in 1990:")
print(dalys_1990)

# Compare mean DALYs between UK and France
uk_data = dalys_data[dalys_data["Entity"] == "United Kingdom"]
france_data = dalys_data[dalys_data["Entity"] == "France"]

uk_mean = uk_data["DALYs"].mean()
france_mean = france_data["DALYs"].mean()
print(f"\nUK mean DALYs: {uk_mean:.2f}")
print(f"France mean DALYs: {france_mean:.2f}")
# Answer: UK mean is higher/lower than France

# Plot UK DALYs over time
plt.figure(figsize=(10, 5))
plt.plot(uk_data["Year"], uk_data["DALYs"], "b+-", label="United Kingdom")
plt.title("DALYs Trend in the United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs (rate)")
plt.xticks(uk_data["Year"], rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("uk_dalys_trend.png")
plt.show()

# Example question implementation
# Question: How do DALYs trends compare between China and India?
china_data = dalys_data[dalys_data["Entity"] == "China"]
india_data = dalys_data[dalys_data["Entity"] == "India"]

plt.figure(figsize=(12, 6))
plt.plot(china_data["Year"], china_data["DALYs"], "r--", label="China")
plt.plot(india_data["Year"], india_data["DALYs"], "g-.", label="India")
plt.title("DALYs Comparison: China vs India (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs (rate)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("china_india_dalys_comparison.png")
plt.show()
