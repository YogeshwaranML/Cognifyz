import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# 2. Identify restaurants with maximum and minimum votes
max_votes_restaurant = df.loc[df['Votes'].idxmax()]
min_votes_restaurant = df.loc[df['Votes'].idxmin()]

print("=== 🏆 Votes Analysis ===")
print(f"Restaurant with Maximum Votes: {max_votes_restaurant['Restaurant Name']} ({max_votes_restaurant['Votes']} votes)")
print(f"Restaurant with Minimum Votes: {min_votes_restaurant['Restaurant Name']} ({min_votes_restaurant['Votes']} votes)")

# 3. Analyze the correlation between votes and rating
correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"\nCorrelation between Votes and Aggregate Rating: {correlation:.2f}")

# 4. Prepare data for 100% Stacked Area Chart
# Create bins for Vote groups
vote_bins = [0, 50, 200, 500, 1000, 15000]
vote_labels = ['0-50', '51-200', '201-500', '501-1000', '1000+']
df['Vote Group'] = pd.cut(df['Votes'], bins=vote_bins, labels=vote_labels, right=False)

# Create categories for Ratings
def rating_category(rating):
    if rating <= 2.5:
        return 'Poor (0-2.5)'
    elif rating <= 3.5:
        return 'Average (2.6-3.5)'
    elif rating <= 4.0:
        return 'Good (3.6-4.0)'
    else:
        return 'Excellent (4.1-5.0)'

df['Rating Category'] = df['Aggregate rating'].apply(rating_category)

# Group data and convert to percentages (row-wise sum to 100%)
grouped = df.groupby(['Vote Group', 'Rating Category']).size().unstack(fill_value=0)
grouped_percent = grouped.div(grouped.sum(axis=1), axis=0) * 100

# Reorder columns logically for the chart
category_order = ['Poor (0-2.5)', 'Average (2.6-3.5)', 'Good (3.6-4.0)', 'Excellent (4.1-5.0)']
grouped_percent = grouped_percent[category_order]

# 5. Plot the 100% Stacked Area Chart
plt.figure(figsize=(12, 7))
colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']

# Use stackplot with the transposed percentage data
plt.stackplot(grouped_percent.index, 
              grouped_percent.T, 
              labels=grouped_percent.columns, 
              colors=colors, 
              alpha=0.8)

# Formatting the chart
plt.title('Rating Distribution by Vote Count Groups (100% Stacked)', 
          fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Number of Votes', fontsize=12, fontweight='bold')
plt.ylabel('Percentage of Restaurants (%)', fontsize=12, fontweight='bold')
plt.legend(title='Rating Categories', loc='upper left', bbox_to_anchor=(1.02, 1))
plt.ylim(0, 100)  # Ensures the Y-axis is exactly 100%
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the chart
plt.show()
