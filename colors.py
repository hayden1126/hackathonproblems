import random

def generate_randomdancefloor(n, m):
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(m)] for _ in range(n)]

def generate_input():
    n = random.randint(3, 100)  # Number of rows
    m = random.randint(3, 100)  # Number of columns
    random_dancefloor = generate_randomdancefloor(n, m)
    return {'n': n, 'm': m, 'dancefloor': random_dancefloor}

n, m, dancefloor = generate_input().values()

print("n =", n)
print("m =", m)
print(dancefloor)


# Solution

from math import floor   

def euclidean_distance(c1, c2):  
    return floor(((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5)  

def find_min_color_change(n, m, dancefloor):  
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    
    # Initialize the distances with infinity  
    distances = [[float('inf')] * m for _ in range(n)]  
    visited = [[False] * m for _ in range(n)]   
    distances[0][0] = 0 # Starting point  

    # Priority queue for the positions to visit, starting with the top-left corner  
    queue = [(0, 0, 0)] # (gradient, row, col)  

    while queue:  
        current_dist, row, col = queue.pop(0)  
        if (visited[row][col]):   
            continue   
        visited[row][col] = True

        # Iterate through possible moves  
        for dr, dc in directions:  
            r, c = row + dr, col + dc  
            if 0 <= r < n and 0 <= c < m:  
                # Calculate the gradient to the next tile  
                gradient = euclidean_distance(dancefloor[row][col], dancefloor[r][c])  
                new_dist = current_dist + gradient  
                # If a shorter path is found, update the distance and add to the queue  
                if new_dist < distances[r][c]:  
                    distances[r][c] = new_dist  
                    queue.append((new_dist, r, c))  
                    # Sort the queue to prioritize the next shortest path. mimics a priority queue's behavior  
                    queue.sort()  

    return distances[-1][-1]

print(find_min_color_change(n, m, dancefloor))
