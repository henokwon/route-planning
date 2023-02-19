
def shortest_route(buildings, start):
    # Initialize an empty dictionary to store the distances between every pair of buildings
    distances = {}
    
    # Iterate over each building
    for building in buildings:
        # Initialize the current distance
        current_distance = 0

        # Iterate over every pair of buildings
        for other_building in buildings:
            if other_building != building:
                # Calculate the distance between the buildings
                distance = calculate_distance(building, other_building)
                # Store the distances in the distances dictionary
                distances[(building, other_building)] = distance
                # Update the current distance
                current_distance += distance
            
        # Add the distance from the start building to the current building
        current_distance += abs(start - building)
        # Store the distances in the distances dictionary
        distances[(start, building)] = abs(start - building)
        
    # Initialize the minimum distance and the optimal route
    min_distance = float("inf")
    optimal_route = []
    
    # Iterate over every permutation of buildings
    for route in permutations(buildings):
        # Initialize the current distance
        current_distance = 0
        
        # Iterate over every pair of buildings in the route
        for i in range(len(route)):
            # Calculate the distance between the current building and the next building
            current_distance += distances[(route[i], route[(i+1) % len(route)])]

        # If the current distance is the smallest, update the minimum distance and the optimal route
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_route = route
    
    # Return the optimal route
    return optimal_route