## Implement a route planning algorithm for a delivery company

A delivery company has to deliver packages to several buildings in a city. Given the set of buildings and the distance between every pair of buildings, the problem is to find the shortest possible route that visits every building exactly once and returns to the starting building.
##

Implement a function that takes a list of buildings and a starting building and returns the shortest possible route to travel from the starting building to all the other buildings, visiting all the buildings exactly once and returning to the starting building.

## The problem and how i approached it

This is a problem known as The Travelling Salesman Problem (TSP). which is an optimization problem that seeks to find the most efficient route for a salesman to visit a given set of cities. The goal is to find the shortest route possible that visits each city only once and returns to the origin. In order to solve the Travelling Salesman Problem, there are a few approaches that can be used.

One way to solve the TSP is through the use of an exact algorithm. This approach is based on the brute-force technique and seeks to find the most optimal solution by comparing all possible routes. This approach can be computationally expensive and require a high degree of processing power.

Another approach is to use a heuristic algorithm. Heuristics algorithms do not guarantee the most optimal solution, but they do provide a good enough solution in a much shorter time frame. By using certain rules, they are able to prune down the search space and provide a good enough solution.

The third approach is to use a meta-heuristic algorithm. Meta-heuristics are more complex and sophisticated algorithms that are able to consider both global and local search techniques. They are able to provide good solutions in a reasonable amount of time.

Finally, the fourth approach is to use an approximation algorithm. This approach will not provide the most optimal solution, but it is able to provide a good enough solution in a shorter amount of time. This approach is often used when time is an issue and the optimal solution is not necessary.

here i used the first approach to solve the problem.

## Test case:

Given a list of buildings `buildings` and a starting point `start`, this program should find the shortest route to traverse all of the buildings.

Inputs:

```
buildings: [2, 3, 4, 5, 6]
start: 7
```

Expected Output:

```
optimal_route: [7, 6, 5, 4, 3, 2]
```

Test Steps:

1. Create a list of buildings `buildings` and a starting point `start`.
2. Call the `shortest_route` function with the list of buildings and starting point as arguments.
3. Assert that the returned `optimal_route` is equal to the expected output `[7, 6, 5, 4, 3, 2]`.

## Time and space complexity analysis

The time complexity of the given code is O(N!), as it has to iterate over every permutation of buildings. The space complexity is O(N^2), as the distance between each pair of buildings has to be stored in a dictionary.
