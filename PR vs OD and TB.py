import pandas as pd

# Load the dataset
# Assuming the file is saved as 'Dataset.csv' in the same directory
df = pd.read_csv(r"C:\Users\mlyog\Downloads\Dataset .csv", encoding='latin-1') # Using latin-1 to avoid utf-8 decoding errors

print("📊 Analysis: Price Range vs. Services Offered 📊\n")

# 1. Table Booking Analysis
# Group by Price range and calculate the percentage of 'Yes' for Table Booking
booking_analysis = df.groupby('Price range')['Has Table booking'].apply(
    lambda x: (x == 'Yes').mean() * 100
).reset_index()
booking_analysis.columns = ['Price Range', 'Table Booking Availability (%)']

print("🍽️ Table Booking Availability by Price Range:")
print(booking_analysis.to_string(index=False))
print("-" * 50)

# 2. Online Delivery Analysis
# Group by Price range and calculate the percentage of 'Yes' for Online Delivery
delivery_analysis = df.groupby('Price range')['Has Online delivery'].apply(
    lambda x: (x == 'Yes').mean() * 100
).reset_index()
delivery_analysis.columns = ['Price Range', 'Online Delivery Availability (%)']

print("🛵 Online Delivery Availability by Price Range:")
print(delivery_analysis.to_string(index=False))
print("-" * 50)

# 3. Overall Conclusion Logic
print("💡 Insight Generation:")
highest_booking = booking_analysis.loc[booking_analysis['Table Booking Availability (%)'].idxmax()]
highest_delivery = delivery_analysis.loc[delivery_analysis['Online Delivery Availability (%)'].idxmax()]

print(f"-> Table Booking is most common in Price Range {int(highest_booking['Price Range'])} ({highest_booking['Table Booking Availability (%)']:.2f}%).")
print(f"-> Online Delivery is most common in Price Range {int(highest_delivery['Price Range'])} ({highest_delivery['Online Delivery Availability (%)']:.2f}%).")