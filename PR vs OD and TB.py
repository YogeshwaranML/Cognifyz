import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================
# Load and Prepare Data
# ============================================
df = pd.read_csv('Dataset .csv')

# Clean data - drop rows with missing price range
df = df.dropna(subset=['Price range'])

# ============================================
# Analyze Table Booking by Price Range
# ============================================
table_booking = df.groupby(['Price range', 'Has Table booking']).size().unstack(fill_value=0)

# ============================================
# Analyze Online Delivery by Price Range
# ============================================
online_delivery = df.groupby(['Price range', 'Has Online delivery']).size().unstack(fill_value=0)

# Print Summary Statistics
print("=" * 55)
print("  PRICE RANGE vs. SERVICE AVAILABILITY")
print("=" * 55)

for pr in sorted(df['Price range'].unique()):
    total = len(df[df['Price range'] == pr])
    tb_yes = len(df[(df['Price range'] == pr) & (df['Has Table booking'] == 'Yes')])
    od_yes = len(df[(df['Price range'] == pr) & (df['Has Online delivery'] == 'Yes')])
    print(f"\n  Price Range {pr} (Total: {total} restaurants)")
    print(f"    Table Booking:   {tb_yes:>5} ({tb_yes/total*100:.1f}%)")
    print(f"    Online Delivery: {od_yes:>5} ({od_yes/total*100:.1f}%)")

# ============================================
# Create Stacked Column Chart
# ============================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- Chart 1: Table Booking ---
if 'No' not in table_booking.columns:
    table_booking['No'] = 0
if 'Yes' not in table_booking.columns:
    table_booking['Yes'] = 0

axes[0].bar(table_booking.index, table_booking['No'], 
            label='No Table Booking', color='#FF6B6B', edgecolor='white')
axes[0].bar(table_booking.index, table_booking['Yes'], 
            bottom=table_booking['No'], label='Has Table Booking', 
            color='#4ECDC4', edgecolor='white')

# Add percentage labels
for i, pr in enumerate(table_booking.index):
    total = table_booking.loc[pr].sum()
    yes_pct = table_booking.loc[pr, 'Yes'] / total * 100
    axes[0].text(i, total + 50, f'{yes_pct:.1f}%', 
                ha='center', fontsize=12, fontweight='bold', color='#2C3E50')

axes[0].set_title('Table Booking by Price Range', fontsize=14, fontweight='bold', pad=15)
axes[0].set_xlabel('Price Range (1=Low → 4=High)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
axes[0].set_xticks([1, 2, 3, 4])
axes[0].legend(loc='upper left')
axes[0].grid(axis='y', alpha=0.3, linestyle='--')

# --- Chart 2: Online Delivery ---
if 'No' not in online_delivery.columns:
    online_delivery['No'] = 0
if 'Yes' not in online_delivery.columns:
    online_delivery['Yes'] = 0

axes[1].bar(online_delivery.index, online_delivery['No'], 
            label='No Online Delivery', color='#FFA07A', edgecolor='white')
axes[1].bar(online_delivery.index, online_delivery['Yes'], 
            bottom=online_delivery['No'], label='Has Online Delivery', 
            color='#98D8C8', edgecolor='white')

# Add percentage labels
for i, pr in enumerate(online_delivery.index):
    total = online_delivery.loc[pr].sum()
    yes_pct = online_delivery.loc[pr, 'Yes'] / total * 100
    axes[1].text(i, total + 50, f'{yes_pct:.1f}%', 
                ha='center', fontsize=12, fontweight='bold', color='#2C3E50')

axes[1].set_title('Online Delivery by Price Range', fontsize=14, fontweight='bold', pad=15)
axes[1].set_xlabel('Price Range (1=Low → 4=High)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
axes[1].set_xticks([1, 2, 3, 4])
axes[1].legend(loc='upper right')
axes[1].grid(axis='y', alpha=0.3, linestyle='--')

plt.suptitle('Price Range vs. Online Delivery & Table Booking', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('price_range_services.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n✅ Stacked column chart generated successfully!")
