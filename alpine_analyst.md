
### Alpine Analyst

It is now holidays, and Vincent loves skiing. Having tried out all the regular routes, he decides to ski down multiple off-piste runs. However, he wants to have an idea of a run's difficulty before going down them. Given an array of altitudes at regular intervals across a slope, help Vincent write a function that evaluates the difficulty of a ski run by identifying the 50-meter segment with largest average steepness. Return the product of the average steepness of this segment and number of troughs in it as the difficulty rating of the entire run. 

This function takes one input: 
- `topography`: A one-dimensional array of integers representing the elevation (in meters) at regular intervals of `1` meter from the start to the end of the slope.

#### Details
- The steepness between 2 adjacent points is the modulus of its gradient.
- The average steepness of a 50-meter segment is the average steepness of the 49 pairs of adjacent points.
- A trough can be found when a point's altitude is lower than that of its adjacent points.
- If there are multiple 50-meter segments with the maximum average steepness, take the number of troughs as the largest one among these 50-meter segments. 
- Round the overall slope grade to two decimal places.

#### Constraints
- The `topography` arrays will contain at least 50 elements and at most 1000 elements.
- All values in `topography` will be positive integers from 0 to 3300.