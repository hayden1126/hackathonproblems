### Dancefloor

Dylan stands at the entrance of a vibrant dancefloor, the final obstacle before his initiation into the enigmatic Harrow Secret Society. The dancefloor is no ordinary space; it's a grid of illuminated tiles, each radiating with a unique color represented by an RGB value. Dylan's challenge is to navigate from the top-left corner of the dancefloor to the VIP section located at the bottom-right corner, choosing his steps wisely to minimize the total color change between consecutive tiles he steps on. 

Given a 2D image represented as a list of lists of tile values, where each value is a tuple representing the RGB color (Red, Green, Blue) of that tile, write a function to find the shortest path from the top-left corner (0,0) to the bottom-right corner (n-1, m-1) of the image. The "distance" between two adjacent pixels is defined as the Euclidean distance between their RGB values rounded down to nearest integer. 

The path can move in four directions at any point: left, right, up, or down, but cannot go diagonally. The goal is to minimize the total gradient (color change) along the path. 

The function takes 3 inputs:  
- n: the number of rows in the dancefloor matrix,   
- m: the number of columns in the dancefloor matrix,   
- dancefloor: a list of lists, where each inner list represents a row of tiles on the dancefloor, and each tile is represented as a tuple `(R, G, B)` indicating the RGB color of the tile. 

The function should return the minimum total gradient (color change) Dylan must traverse to reach the VIP section. (Hint: Dijkstra) 

#### Constraints

- `3 ≤ n, m ≤ 100`
- The RGB values are integers between `0` and `255`, inclusive.