import numpy as np
import matplotlib.pyplot as plt

# Define land use categories
land_use_categories = {
    0: "Empty",
    1: "Residential",
    2: "Commercial",
    3: "Industrial",
    4: "Green Space"
}

# Generate a random city grid
np.random.seed(42)
city_grid = np.random.choice(list(land_use_categories.keys()), size=(20, 20), p=[0.1, 0.4, 0.2, 0.2, 0.1])

# Calculate usage statistics
unique, counts = np.unique(city_grid, return_counts=True)
total_cells = city_grid.size
usage_stats = {land_use_categories[k]: v / total_cells * 100 for k, v in zip(unique, counts)}

# Display stats
print("Urban Land Use Performance Report:")
for category, percent in usage_stats.items():
    print(f"{category:12}: {percent:.2f}%")

# Target distribution for ideal urban planning
target_distribution = {
    "Residential": 35,
    "Commercial": 20,
    "Industrial": 15,
    "Green Space": 25,
    "Empty": 5
}

# Calculate deviation score
score = 0
for category in target_distribution:
    actual = usage_stats.get(category, 0)
    target = target_distribution[category]
    score += abs(actual - target)

print(f"\nTotal Deviation Score: {score:.2f} (Lower is better)")

# Plot the bar chart
categories = list(target_distribution.keys())
actual_values = [usage_stats.get(cat, 0) for cat in categories]
target_values = [target_distribution[cat] for cat in categories]

x = np.arange(len(categories))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, actual_values, width, label='Actual Usage %')
plt.bar(x + width/2, target_values, width, label='Target Usage %')

plt.ylabel('Percentage')
plt.title('Urban Land Use Distribution')
plt.xticks(x, categories, rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show(block=False)
plt.pause(3)
plt.close()

# Optional: Plot heatmap of the city grid
plt.figure(figsize=(6, 6))
cmap = plt.colormaps.get_cmap('tab20', len(land_use_categories))
plt.imshow(city_grid, cmap=cmap)
cbar = plt.colorbar(ticks=range(len(land_use_categories)))
cbar.ax.set_yticklabels([land_use_categories[i] for i in range(len(land_use_categories))])
plt.title("City Grid Land Use Map")
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.show(block=False)
plt.pause(3)
plt.close()
