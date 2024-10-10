from puzzle import Puzzle, generate_random_initial_state
from astar import *

if __name__ == "__main__":
    while True: 
        random_state = generate_random_initial_state()  
        puzzle = Puzzle(random_state)  
        
        if puzzle.is_solvable(): 
            print("The generated state is solvable.")
            print("Initial State:")
            puzzle.display()  
            break 
        else:
            print("The generated state is not solvable. Generating a new state...")
    
    
    print("Initial State:")
    puzzle.display()
    
    result = astar(puzzle)
    
    if result != "No solution found":
        print("Solution Path:")
        for i, state in enumerate(result):
            print(f"Step {i}:")
            for row in state:
                print(" ".join(str(x) if x != 0 else " " for x in row)) 
            print("\n" + "-"*10) 
    else:
        print(result)