import random

current_elevation = 2900
adjusted_input = []

for _ in range(200):
    # Introducing a bit of a variation to sometimes go up, but mostly go down
    direction = random.choice([1, -1, -1, -1, -1])  # More likely to go down
    distance = [random.randint(0, 5), random.randint(5, 7), random.randint(7, 20)][random.choice([0, 0, 0, 0, 1, 1, 2])]
    delta = distance * direction
    
    # Ensuring the new point is within the elevation limits
    new_elevation = max(0, min(3000, current_elevation + delta))
    adjusted_input.append(new_elevation)
    current_elevation = new_elevation

print(adjusted_input)