### Enclosed Area in an Irregular Polygon

Given a 2D grid of characters with `#` representing the edges of a concave polygon and `.` representing empty space, write a function to compute the area enclosed by the polygon. The grid will not contain any "holes" (i.e., areas enclosed by `#` that are not part of the outer boundary), and the polygon's edges will not cross themselves. The input grid is a rectangular list of strings, where each string represents a row of the grid.

#### Input:

- **grid** (List of Strings): A list where each element is a string that represents a row of the grid. Each string consists of `#` (edge) and `.` (empty space).

#### Output:

- **int**: The area enclosed by the polygon, i.e., the number of `.` characters that are enclosed by `#` characters.

#### Constraints:

- The polygon is always closed and does not cross itself.
- The grid dimensions are at least 1x1 and at most 100x100.
- There are no "holes" in the polygon.
- The edges of the polygon (`#`) form a continuous line that defines the boundary of the enclosed area.

#### Example:

**Input:**

```
[
"####",
"#..#",
"####"
]
```

**Output:**

```
2
```

#### Explanation:

In the given grid, there are 2 dots (`.`) enclosed by the hash (`#`) characters, which represent the edges of the polygon. Thus, the enclosed area is 2.

---

### Implementation Notes:

- You may assume that the input grid is always valid and satisfies the constraints mentioned.
- The polygon can be concave, but the provided algorithm should correctly compute the enclosed area regardless of its shape.