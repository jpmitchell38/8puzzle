class Puzzle:
    def __init__(self, state):
        self.state = state
        self.empty_pos = self.find_empty()
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

    def is_solved(self):
        return self.state == self.goal_state

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty_pos
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        
        for dx, dy in possible_moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state] 
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                neighbors.append(Puzzle(new_state))
        
        return neighbors

    def display(self):
        for row in self.state:
            print(row)
        print()