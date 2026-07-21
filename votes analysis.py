import pandas as pd

# Load the dataset
# Assuming the file is saved as 'Dataset.csv' in the same directory
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv", encoding='utf-8') # Use encoding='latin-1' if utf-8 throws an error

# Task 2.1: Identify restaurants with maximum and minimum votes
max_votes = df.loc[df['Votes'].idxmax()]
min_votes = df.loc[df['Votes'].idxmin()]

print("🏆 Restaurant with MAXIMUM Votes 🏆")
print(f"Name      : {max_votes['Restaurant Name']}")
print(f"Votes     : {max_votes['Votes']}")
print(f"Rating    : {max_votes['Aggregate rating']}")
print("-" * 40)

print("📉 Restaurant with MINIMUM Votes 📉")
print(f"Name      : {min_votes['Restaurant Name']}")
print(f"Votes     : {min_votes['Votes']}")
print(f"Rating    : {min_votes['Aggregate rating']}")
print("-" * 40)

# Task 2.2: Analyze correlation between Votes and Rating
correlation = df['Votes'].corr(df['Aggregate rating'])

print(f"🔗 Correlation between Votes and Aggregate Rating: {correlation:.2f}")

# Interpretation
if correlation > 0.5:
    print("💡 Insight: There is a strong positive correlation. More votes generally mean higher ratings.")
elif 0 < correlation <= 0.5:
    print("💡 Insight: There is a weak positive correlation. Votes slightly influence the rating.")
elif correlation == 0:
    print("💡 Insight: No correlation exists between votes and ratings.")
else:
    print("💡 Insight: There is a negative correlation. More votes tend to relate to lower ratings.")