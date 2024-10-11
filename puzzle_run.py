import argparse

from puzzle import Puzzle, generate_random_initial_state
from astar import *
from bfs import *

if __name__ == "__main__":
    # A* - Completed
    #BFS - Completed
    #DPS - 
    #Greedy - 
    #UCS - 
    print("\n\n")
    parser = argparse.ArgumentParser(description="8-puzzle solver")
    parser.add_argument("-a", action="store_true", help="Display full A* solution steps")
    # parser.add_argument("-b", action="store_true", help="Display every 10000 BFS solution steps")

    
    args = parser.parse_args()
    
    while True: 
        random_state = generate_random_initial_state()  
        puzzle = Puzzle(random_state)  
        
        if puzzle.is_solvable(): 
            print("The generated state is solvable.")
            print("\nInitial State:")
            puzzle.display()  
            break 
        else:
            print("The generated state is not solvable. Generating a new state...")
    
    result = astar(puzzle)
    step_count = len(result) - 1
    
    # Display the full A* solution steps if -a is set
    if args.a:
        print("\n \n" + "-"*10) 
        print("Solution Path to A*:")
        for i, state in enumerate(result):
            print(f"\nStep {i}:")
            for row in state:
                print(" ".join(str(x) if x != 0 else " " for x in row)) 
        print("-"*10) 
    else:        
        print("\nFinal State:")
        final_state = result[-1]
        for row in final_state:
            print(" ".join(str(x) if x != 0 else " " for x in row)) 
        # print("\n" + "-"*10)
        
    print("\nA* number of steps to complete:", step_count)
        
    # BFS algorithm
    # result = bfs(puzzle, display_steps=args.b) 
    result = bfs(puzzle) 
    step_count1, solution_path = result 

    # if args.b:
    #     pass
    # else:    
    #     pass    
    #     # print("\nFinal State:")
    #     # final_state = solution_path[-1]  
    #     # for row in final_state.state:  
    #     #     print(" ".join(str(x) if x != 0 else " " for x in row)) 
    #     # print("\n" + "-" * 10)
            
    print("BFS number of steps to complete:", step_count1)
        
    