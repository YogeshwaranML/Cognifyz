import pandas as pd

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv")

# 2. Drop rows with missing 'City' or 'Aggregate rating' to ensure clean math
df = df.dropna(subset=['City', 'Aggregate rating'])

# 3. Identify the city with the most restaurants
city_counts = df['City'].value_counts()
top_city_by_count = city_counts.idxmax()
top_city_count = city_counts.max()

print(f"🏙️ City with the most restaurants: {top_city_by_count} ({top_city_count} restaurants)\n")

# 4. Calculate the average rating for restaurants in each city
avg_rating_per_city = df.groupby('City')['Aggregate rating'].mean()

print("⭐ Top 5 Cities by Average Rating:")
# Sort values to see the top-rated cities
print(avg_rating_per_city.sort_values(ascending=False).head(5))
print("-" * 40)

# 5. Identify the city with the highest average rating
top_city_by_rating = avg_rating_per_city.idxmax()
highest_avg_rating = avg_rating_per_city.max()

print(f"🏆 City with the highest average rating: {top_city_by_rating} (Rating: {highest_avg_rating:.2f})")