# 8puzzle

This project is an implementation of the classic 8-Puzzle problem, a sliding puzzle consisting of 8 numbered tiles arranged on a 3x3 grid. The goal is to move the tiles to achieve the correct order (from 1 to 8, with one empty space) using the fewest moves possible.
<br><br>
## Features

Searching algorithms
- Breadth-First Search (BFS): An uninformed search algorithm that explores all possible moves layer by layer
- A*: An informed search algorithm using heuristics to efficiently find the optimal solution. <br>

Path
- Given a certain parameter (-a), you can see the full path of A*
- Since BFS takes an extreme amount of steps to find a solution, You cannot get the full path of BFS
<br><br>
## How it Works

1) The initial puzzle state randomly generated and checks to see if the puzzle is solvable, if not, generates a new puzzle.
2) The BFS and A* algorithm explores the puzzle states to find a solution.
3) The number of steps are displayed. BFS may explore more nodes due to its exhaustive nature, while A* finds a solution more efficiently by using heuristics.

Standard run screenshot

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
    <img src="docs/Screenshot 2024-10-16 170055.png" alt="Graph 1" style="width: 25%; margin-bottom: 10px;" />
</div>

A* path run screenshot

<div style="display: flex; flex-wrap: wrap;">
    <img src="docs/Screenshot 2024-10-16 170628.png" alt="Graph 2" style="width: 28%; margin-bottom: 10px;" />
    <img src="docs/Screenshot 2024-10-16 170644.png" alt="Graph 3" style="width: 25%; margin-bottom: 10px;" />
</div>