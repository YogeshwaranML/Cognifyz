import pandas as pd
import matplotlib.pyplot as plt

# ---- Step 1: Load the dataset ----
df = pd.read_csv('Dataset .csv')

# ---- Step 2: Clean data ----
df = df.dropna(subset=['City', 'Aggregate rating', 'Rating text'])

# ---- Step 3: Task 1 - City with most restaurants ----
city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()
print(f"✅ City with Most Restaurants: {top_city} ({city_counts.max()} restaurants)")

# ---- Step 4: Task 2 - Average rating per city ----
avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print("\n📍 Average Rating per City (Top 10):")
print(avg_rating.head(10).round(2))

# ---- Step 5: Task 3 - City with highest average rating ----
# Filter cities with at least 5 restaurants for fairness
city_filtered = df.groupby('City').filter(lambda x: len(x) >= 5)
top_rated_city = city_filtered.groupby('City')['Aggregate rating'].mean().idxmax()
top_rated_value = city_filtered.groupby('City')['Aggregate rating'].mean().max()
print(f"\n🏆 Highest Avg Rating City: {top_rated_city} ({top_rated_value:.2f})")

# ---- Step 6: Prepare data for STACKED BAR CHART ----
top_cities = city_counts.head(15).index.tolist()
df_top = df[df['City'].isin(top_cities)]

# Group by City and Rating text
stacked_data = df_top.groupby(['City', 'Rating text']).size().unstack(fill_value=0)

# Reorder columns by rating quality
rating_order = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor', 'Not rated']
rating_order = [r for r in rating_order if r in stacked_data.columns]
stacked_data = stacked_data[rating_order]

# ---- Step 7: Plot STACKED BAR CHART ----
colors = {
    'Excellent':  '#1a7a3a',
    'Very Good':  '#4CAF50',
    'Good':       '#FFC107',
    'Average':    '#FF9800',
    'Poor':       '#F44336',
    'Not rated':  '#BDBDBD'
}

fig, ax = plt.subplots(figsize=(14, 8))

bottom = [0] * len(stacked_data)
for rating in rating_order:
    ax.bar(stacked_data.index, stacked_data[rating], 
           bottom=bottom, label=rating, 
           color=colors.get(rating, '#999'), edgecolor='white', width=0.7)
    bottom = [b + v for b, v in zip(bottom, stacked_data[rating])]

# Styling
ax.set_title('🏙️ Restaurant Count by City (Stacked by Rating Category)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('City', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
ax.legend(title='Rating Category', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Save and show
plt.savefig('city_analysis_stacked.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n✅ Stacked bar chart generated successfully!")
