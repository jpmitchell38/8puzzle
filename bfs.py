from collections import deque

# def bfs(initial_puzzle, display_steps=False):
def bfs(initial_puzzle):
    # if not initial_puzzle.is_solvable():
    #     print("Puzzle is not solvable.")
    #     return None

    frontier = deque([(initial_puzzle, [])])
    frontier_set = {initial_puzzle} 
    explored = set()
    iterations = 0

    while frontier:
        iterations += 1
        current_puzzle, path = frontier.popleft()
        frontier_set.remove(current_puzzle)

        if current_puzzle.is_solved():
            # print(f"Solved in {iterations} iterations!")
            return iterations, path + [current_puzzle] 

        explored.add(current_puzzle)

        for neighbor in current_puzzle.get_neighbors():
            if neighbor not in explored and neighbor not in frontier_set:
                frontier.append((neighbor, path + [current_puzzle]))
                frontier_set.add(neighbor)

        # if display_steps and iterations % 10000 == 0:
        #     print(f"\nIteration {iterations}:")
        #     current_puzzle.display() 

    print("No solution found.")
    return None