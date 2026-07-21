import pandas as pd

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# 2. Drop rows with missing cuisines
df = df.dropna(subset=['Cuisines'])

# 3. Split cuisines and create a flat list
all_cuisines = []
for cuisines in df['Cuisines']:
    # Split by comma and strip whitespace
    items = [c.strip() for c in cuisines.split(',')]
    all_cuisines.extend(items)

# 4. Count cuisine frequencies
cuisine_counts = pd.Series(all_cuisines).value_counts()

# 5. Get top 3 cuisines
top_3 = cuisine_counts.head(3)
print("Top 3 Most Common Cuisines:\n")
print(top_3)

# 6. Calculate percentage of restaurants serving each top cuisine
total_restaurants = len(df)
print("\nPercentage of Restaurants Serving Each Top Cuisine:\n")
for cuisine, count in top_3.items():
    # Count restaurants that have this cuisine in their list
    restaurants_with_cuisine = df['Cuisines'].str.contains(cuisine, case=False, na=False).sum()
    percentage = (restaurants_with_cuisine / total_restaurants) * 100
    print(f"{cuisine}: {restaurants_with_cuisine} restaurants ({percentage:.2f}%)")

# 7. Optional: Visualize with a bar chart
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
top_3.plot(kind='bar', color=['#FFD700', '#C0C0C0', '#CD7F32'])
plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()