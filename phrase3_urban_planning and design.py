import numpy as np
import matplotlib.pyplot as plt

# Constants
GRID_SIZE = 20  # Size of the city grid
MAX_DENSITY = 100  # Max population density per unit
GREEN_RATIO = 0.2  # Ideal green space ratio
INFRA_QUALITY_TARGET = 0.7  # Minimum acceptable infrastructure quality

# Simulate city layout
def generate_city(grid_size):
    population_density = np.random.randint(0, MAX_DENSITY, (grid_size, grid_size))
    green_space = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])
    infrastructure_quality = np.random.rand(grid_size, grid_size)
    return population_density, green_space, infrastructure_quality

# Score the city layout
def score_city(pop_density, green_space, infra_quality):
    avg_density = np.mean(pop_density)
    green_ratio = np.mean(green_space)
    infra_score = np.mean(infra_quality)
    
    score = 100
    if avg_density > 70:
        score -= (avg_density - 70) * 0.5
    if green_ratio < GREEN_RATIO:
        score -= (GREEN_RATIO - green_ratio) * 100
    if infra_score < INFRA_QUALITY_TARGET:
        score -= (INFRA_QUALITY_TARGET - infra_score) * 100

    return max(score, 0)

# Visualization
def visualize_city(pop_density, green_space):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(pop_density, cmap='hot')
    plt.title("Population Density")
    plt.colorbar()
    
    plt.subplot(1, 2, 2)
    plt.imshow(green_space, cmap='Greens')
    plt.title("Green Spaces")
    plt.colorbar()
    
    plt.tight_layout()
    plt.show()

# Main execution
population_density, green_space, infrastructure_quality = generate_city(GRID_SIZE)
city_score = score_city(population_density, green_space, infrastructure_quality)
visualize_city(population_density, green_space)

print("City Planning Quality Score: {city_score:.2f}/100")