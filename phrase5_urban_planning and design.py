def classify_area(population, area):
    density = population / area
    print(f"\nPopulation Density: {density:.2f} people/km²")

    if density < 300:
        print("Status: Underutilized land.")
        print("Suggestion: Suitable for residential development.")
    elif density < 1000:
        print("Status: Moderately populated.")
        print("Suggestion: Ideal for mixed-use development.")
    else:
        print("Status: Highly congested.")
        print("Suggestion: Consider vertical development and congestion control.")

# Main Program
print("Urban Planning and Design System")

try:
    population = int(input("Enter total population: "))
    area = float(input("Enter area (in square kilometers): "))
    classify_area(population, area)
except ValueError:
    print("Invalid input. Please enter numeric values for population and area.")
