
def test_shortest_route():
    # Test case 1
    buildings1 = [5, 10, 15]
    start1 = 0
    solution1 = [0, 5, 10, 15]
    assert shortest_route(buildings1, start1) == solution1
    
    # Test case 2
    buildings2 = [20, 25, 30]
    start2 = 15
    solution2 = [15, 20, 25, 30]
    assert shortest_route(buildings2, start2) == solution2
    
    print("All tests passed!")

test_shortest_route()
