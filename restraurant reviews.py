import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# Filter out 'Not rated' restaurants for accurate text analysis
df = df[df['Rating text'] != 'Not rated'].copy()

# 2. Identify the most common positive and negative keywords
positive_keywords = ['Excellent', 'Very Good', 'Good']
negative_keywords = ['Poor', 'Average']

pos_counts = df[df['Rating text'].isin(positive_keywords)]['Rating text'].value_counts()
neg_counts = df[df['Rating text'].isin(negative_keywords)]['Rating text'].value_counts()

print("🌟 Most Common Positive Keywords:\n", pos_counts)
print("\n⚠️ Most Common Negative Keywords:\n", neg_counts)

# 3. Calculate the average length of reviews
# Using the 'Rating text' as the review text proxy
df['Review Length'] = df['Rating text'].apply(len)
avg_length = df['Review Length'].mean()

print(f"\n📏 Average Review Length: {avg_length:.2f} characters")

# 4. Explore the relationship between review length and aggregate rating
plt.figure(figsize=(10, 6))
sns.boxplot(x='Aggregate rating', y='Review Length', data=df, palette='viridis')
plt.title("Relationship Between Review Length and Aggregate Rating", fontsize=14, fontweight='bold')
plt.xlabel("Aggregate Rating (0 to 5)", fontsize=12)
plt.ylabel("Review Length (Character Count)", fontsize=12)
plt.tight_layout()
plt.show()