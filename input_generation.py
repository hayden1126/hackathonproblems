import random

current_elevation = random.randint(2200, 3200)
adjusted_input = []

length = random.randint(50, 1000)

for _ in range(length):
    # Introducing a bit of a variation to sometimes go up, but mostly go down
    direction = random.choice([1, -1, -1, -1, -1])  # More likely to go down
    distance = [random.randint(0, 5), random.randint(5, 7), random.randint(7, 20)][random.choice([0, 0, 0, 0, 1, 1, 2])]
    delta = distance * direction
    
    # Ensuring the new point is within the elevation limits
    new_elevation = max(0, min(3300, current_elevation + delta))
    adjusted_input.append(new_elevation)
    current_elevation = new_elevation

print(adjusted_input)


def ski_run_difficulty(topography):
    # Calculate steepness between adjacent points
    steepness = [abs(topography[i] - topography[i+1]) for i in range(len(topography)-1)]
    
    # Initialize variables to track the highest average steepness and its trough count
    max_avg_steepness = 0
    max_trough_count = 0
    
    # Iterate through the array to find the segment with the highest average steepness
    for i in range(len(steepness) - 48):  # Ensure the segment is 50 meters long
        segment = steepness[i:i+50]
        avg_steepness = sum(segment) / 49  # Average steepness of the segment
        trough_count = 0
        
        # Count troughs in the current segment
        for j in range(1, 49):  # Compare each point with its neighbors within the segment
            if topography[i+j] < topography[i+j-1] and topography[i+j] < topography[i+j+1]:
                trough_count += 1
        
        # Update max average steepness and trough count if the current segment is steeper
        if avg_steepness > max_avg_steepness:
            max_avg_steepness = avg_steepness
            max_trough_count = trough_count
        elif avg_steepness == max_avg_steepness:  # If equal, consider the one with more troughs
            max_trough_count = max(max_trough_count, trough_count)
    
    # Calculate difficulty rating
    difficulty_rating = max_avg_steepness * max_trough_count
    
    # Return difficulty rating rounded to three decimal places
    return round(difficulty_rating, 2)

print(ski_run_difficulty(adjusted_input))