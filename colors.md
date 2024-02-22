### Vincent's Dancefloor Dash

Vincent stands at the entrance of a vibrant dancefloor, the final obstacle before his initiation into the enigmatic Harrow Secret Society. The dancefloor is no ordinary space; it's a grid of illuminated tiles, each radiating with a unique color represented by an RGB value. Vincent's challenge is to navigate from the top-left corner of the dancefloor to the VIP section located at the bottom-right corner, choosing his steps wisely to minimize the total change in color between consecutive tiles he steps on.

Given a 2D image represented as a matrix of tile values, where each value is a tuple representing the RGB color (Red, Green, Blue) of that tile, write a function to find the shortest path from the top-left corner (0,0) to the bottom-right corner (n-1, m-1) of the image. The "distance" between two adjacent pixels is defined as the Euclidean distance between their RGB values rounded down to nearest integer.

The path can move in four directions at any point: left, right, up, or down, but cannot go diagonally. The goal is to minimize the total gradient (color change) along the path.

The function takes 3 inputs: 
- n: the number of rows in the dancefloor matrix,  
- m: the number of columns in the dancefloor matrix,  
- dancefloor: a list of lists, where each inner list represents a row of tiles on the dancefloor, and each tile is represented as a tuple `(R, G, B)` indicating the RGB color of the tile.

The function should return the minimum total gradient (color change) Vincent must traverse to reach the VIP section, rounded to a whole number.

<!-- #### Function Signature

```python
def find_min_color_change(n: int, m: int, dancefloor: List[List[Tuple[int, int, int]]]) -> float:
``` -->

### Constraints

- `1 ≤ n, m ≤ 100`
- The RGB values are integers between `0` and `255`, inclusive.


### Example

#### Input

```python
n = 3
m = 3
dancefloor = [
    [(255, 0, 0), (255, 255, 0), (0, 255, 0)],
    [(0, 0, 255), (255, 255, 255), (0, 255, 255)],
    [(0, 0, 0), (255, 0, 255), (0, 0, 255)]
]
```

#### Output

```python
result = 1020.0
```

### Notes
- The problem can be approached by modeling the dancefloor as a graph, where each tile is a node and the edges between nodes represent possible steps with weights equal to the color gradient between them. Algorithms like Dijkstra's or A* are suitable for finding the shortest path with the minimum total gradient.
