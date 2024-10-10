from puzzle import Puzzle
import heapq

def manhattan_heuristic(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_x, goal_y = divmod(tile - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def astar(puzzle):
    start_state = puzzle.state
    goal_state = puzzle.goal_state
    frontier = []
    
    heapq.heappush(frontier, (0, 0, id(puzzle), puzzle))  
    
    explored = set()
    parent_map = {}  
    parent_map[tuple(map(tuple, puzzle.state))] = None 

    while frontier:
        priority, g_cost, _, current_puzzle = heapq.heappop(frontier)
        current_state = tuple(map(tuple, current_puzzle.state))
        
        if current_puzzle.is_solved():
            return reconstruct_path(current_puzzle, parent_map)
        
        explored.add(current_state)
        
        for neighbor in current_puzzle.get_neighbors():
            neighbor_state = tuple(map(tuple, neighbor.state))
            if neighbor_state not in explored:
                h_cost = manhattan_heuristic(neighbor.state, goal_state)
                new_g_cost = g_cost + 1  
                heapq.heappush(frontier, (new_g_cost + h_cost, new_g_cost, id(neighbor), neighbor))
                parent_map[neighbor_state] = current_puzzle  
    
    return "No solution found"

def reconstruct_path(puzzle, parent_map):
    path = []
    current_state = tuple(map(tuple, puzzle.state))

    while current_state is not None:
        path.append(current_state)
        current_state = parent_map[current_state] 
        if current_state is not None:
            current_state = tuple(map(tuple, current_state.state))

    path.reverse() 
    return path