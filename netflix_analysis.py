import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Show basic info
print("Dataset Info:")
print(df.info())

# Count of content by type
type_count = df['type'].value_counts()
print("\nContent Types:\n", type_count)

# Top 10 countries with most content
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 Countries:\n", top_countries)

# Plotting
plt.figure(figsize=(8,5))
top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")
plt.show()