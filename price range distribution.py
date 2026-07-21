import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# 2. Drop rows with missing 'Price range' to ensure accurate counting
df = df.dropna(subset=['Price range'])

# 3. Calculate the count of restaurants in each price range
price_counts = df['Price range'].value_counts().sort_index()
total_restaurants = len(df)

# 4. Calculate the percentage of restaurants for each price range
price_percentage = (price_counts / total_restaurants) * 100

print("📊 Price Range Distribution:\n")
print(price_counts)
print("\n📉 Percentage of Restaurants in Each Price Range:\n")
print(price_percentage.round(2).astype(str) + '%')

# 5. Visualize the distribution using a Bar Chart
plt.figure(figsize=(8, 5))
colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c'] # Green, Blue, Yellow, Red
bars = plt.bar(price_counts.index, price_counts.values, color=colors, edgecolor='black')

# Add labels and title
plt.title("Distribution of Restaurant Price Ranges", fontsize=14, fontweight='bold')
plt.xlabel("Price Range (1 = Low, 4 = Luxury)", fontsize=12)
plt.ylabel("Number of Restaurants", fontsize=12)
plt.xticks(price_counts.index)

# Add percentage labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    pct = (yval / total_restaurants) * 100
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50, f'{pct:.1f}%', 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()