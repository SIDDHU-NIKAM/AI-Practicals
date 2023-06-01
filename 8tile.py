from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the empty space

# Define the possible moves
moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Calculate the Manhattan distance heuristic
def calculate_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# A* search algorithm
def solve_puzzle(start_state):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_state))
    
    while not queue.empty():
        _, current_state = queue.get()
        
        if current_state == goal_state:
            return current_state  # Puzzle solved
        
        visited.add(tuple(map(tuple, current_state)))  # Convert to tuple for hashing
        
        empty_row, empty_col = find_empty_space(current_state)
        
        for move in moves:
            new_row = empty_row + move[0]
            new_col = empty_col + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in current_state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                
                if tuple(map(tuple, new_state)) not in visited:
                    priority = calculate_manhattan_distance(new_state)
                    queue.put((priority, new_state))
                    visited.add(tuple(map(tuple, new_state)))
    
    return None  # No solution found

# Find the coordinates of the empty space (0)
def find_empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Example usage
start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]  # Initial state
solution = solve_puzzle(start_state)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")
