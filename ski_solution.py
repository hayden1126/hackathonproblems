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

topography = [2893, 2876, 2875, 2871, 2866, 2860, 2863, 2863, 2860, 2860, 2857, 2852, 2833, 2833, 2829, 2812, 2810, 2812, 2799, 2796, 2791, 2786, 2782, 2775, 2769, 2764, 2759, 2755, 2751, 2756, 2750, 2745, 2746, 2740, 2734, 2727, 2727, 2726, 2723, 2717, 2720, 2719, 2729, 2724, 2731, 2725, 2711, 2701, 2700, 2696, 2693, 2675, 2661, 2643, 2645, 2654, 2642, 2625, 2622, 2619, 2633, 2627, 2622, 2616, 2611, 2604, 2597, 2590, 2586, 2586, 2576, 2572, 2568, 2563, 2563, 2561, 2556, 2552, 2545, 2539, 2539, 2540, 2542, 2539, 2534, 2529, 2522, 2511, 2510, 2506, 2501, 2495, 2475, 2480, 2474, 2477, 2482, 2477, 2472, 2472, 2473, 2466, 2464, 2458, 2453, 2453, 2448, 2442, 2441, 2434, 2430, 2426, 2415, 2422, 2421, 2409, 2402, 2397, 2397, 2410, 2403, 2402, 2401, 2396, 2391, 2384, 2384, 2378, 2380, 2374, 2368, 2366, 2363, 2360, 2357, 2355, 2337, 2336, 2331, 2329, 2323, 2323, 2303, 2301, 2294, 2289, 2284, 2279, 2277, 2272, 2268, 2271, 2266, 2261, 2260, 2247, 2242, 2235, 2223, 2218, 2203, 2199, 2194, 2194, 2188, 2187, 2187, 2168, 2153, 2155, 2138, 2118, 2116, 2110, 2103, 2108, 2108, 2102, 2107, 2110, 2116, 2113, 2108, 2103, 2090, 2089, 2084, 2077, 2057, 2052, 2050, 2041, 2034, 2036, 2040, 2044, 2055, 2050, 2047, 2054]
print(ski_run_difficulty(topography))