import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# 2. Drop rows with missing 'Has Online delivery' or 'Aggregate rating'
df = df.dropna(subset=['Has Online delivery', 'Aggregate rating'])

# 3. Determine the percentage of restaurants that offer online delivery
delivery_counts = df['Has Online delivery'].value_counts()
total_restaurants = len(df)

# Calculate percentage for 'Yes'
delivery_yes = delivery_counts.get('Yes', 0)
delivery_percentage = (delivery_yes / total_restaurants) * 100

print(f"🛵 Percentage of restaurants that offer online delivery: {delivery_percentage:.2f}%\n")

# 4. Compare the average ratings of restaurants with and without online delivery
avg_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("⭐ Average Ratings Comparison:")
print(avg_ratings)
print("-" * 40)

# 5. Visualize the comparison using a Bar Chart
plt.figure(figsize=(7, 5))
colors = ['#e74c3c', '#2ecc71'] # Red for No, Green for Yes
bars = plt.bar(avg_ratings.index, avg_ratings.values, color=colors, edgecolor='black')

# Add labels and title
plt.title("Average Ratings: Online Delivery vs. No Online Delivery", fontsize=13, fontweight='bold')
plt.xlabel("Has Online Delivery?", fontsize=12)
plt.ylabel("Average Rating", fontsize=12)
plt.ylim(0, 5) # Ratings are out of 5

# Add data labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.2f}', 
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()