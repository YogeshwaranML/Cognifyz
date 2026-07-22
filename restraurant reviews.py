import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 1. Load the dataset
df = pd.read_csv('Dataset .csv')

# 2. Clean data: Remove 'Not rated' reviews for accurate text analysis
df = df[df['Rating text'] != 'Not rated'].copy()

# 3. Analyze text reviews for keywords
all_text = " ".join(df['Rating text'])
words = all_text.split()
common_keywords = Counter(words).most_common(5)

print("📝 Most Common Review Keywords:")
for word, count in common_keywords:
    print(f" - {word}: {count}")

# 4. Calculate average length of reviews
df['Review Length'] = df['Rating text'].apply(len)
avg_length = df['Review Length'].mean()
print(f"\n📏 Average Length of Reviews: {avg_length:.2f} characters")

# 5. Relationship between review length and rating
rating_length = df.groupby('Rating text')['Review Length'].mean().sort_values(ascending=False)
print("\n📊 Relationship between Rating Text and Length:")
print(rating_length)

# 6. Categorize for Donut Chart
def get_sentiment(text):
    if text in ['Excellent', 'Very Good', 'Good']:
        return 'Positive'
    elif text in ['Poor', 'Average']:
        return 'Negative'
    return 'Neutral'

df['Sentiment'] = df['Rating text'].apply(get_sentiment)
sentiment_counts = df['Sentiment'].value_counts()

# 7. Plotting the Donut Chart
plt.figure(figsize=(8, 6))
colors = ['#2ecc71', '#e74c3c', '#f1c40f'] # Green for Positive, Red for Negative

# Create pie chart
wedges, texts, autotexts = plt.pie(
    sentiment_counts, 
    labels=sentiment_counts.index,
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90,
    pctdistance=0.85,
    wedgeprops={'width': 0.4, 'edgecolor': 'white'} # Width makes it a donut
)

# Add center text
plt.text(0, 0, 'Review\nSentiment', ha='center', va='center', fontsize=14, fontweight='bold', color='#333')

# Formatting
plt.title('Distribution of Restaurant Review Sentiments', pad=20, fontsize=16, fontweight='bold')
plt.setp(autotexts, size=12, weight='bold', color='white')
plt.tight_layout()
plt.show()
