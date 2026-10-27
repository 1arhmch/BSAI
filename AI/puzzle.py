
import numpy as np

# Current state
state = np.array([
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 3]
])

# Goal state
goal = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

print("Current State:")
print(state)

# Find blank position
position = np.argwhere(state == 0)[0]
row, col = int(position[0]), int(position[1])

print("Blank position:", row, col)

# Make a copy of the state
new_state = state.copy()

# Move blank Down
new_row = row + 1
new_col = col

if new_row < new_state.shape[0]:
    new_state[row, col], new_state[new_row, new_col] = (
        new_state[new_row, new_col],
        new_state[row, col]
    )
    print("After moving Down:")
    print(new_state)
else:
    print("Illegal move")

print("Goal State:")
print(goal)

print("Original state unchanged:")
print(state)

