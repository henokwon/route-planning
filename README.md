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

