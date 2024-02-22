from math import floor   

def euclidean_distance(c1, c2):  
    return floor(((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5)  

def find_min_color_change(n, m, dancefloor):  
    # Directions: Right, Left, Down, Up  
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
                    # Sort the queue to prioritize the next shortest path. This mimics a priority queue's behavior  
                    queue.sort()  

    # The distance to the bottom-right corner is the answer  

    return distances[-1][-1]



n = 25
m = 44
dancefloor = []
print(find_min_color_change(n, m, dancefloor))