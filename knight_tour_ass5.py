def is_valid(x, y, board, N):
  return 0 <= x < N and 0 <= y < N and board[x][y] == -1
  
def print_solution(board, N):
  for row in board:
    for cell in row:
      print(f"{cell:2}", end=" ")
    print()
    
def solve_knights_tour(N, start_x, start_y):
  board = [[-1 for _ in range(N)] for _ in range(N)]
  move_x = [2, 1, -1, -2, -2, -1, 1, 2]
  move_y = [1, 2, 2, 1, -1, -2, -2, -1]
  board[start_x][start_y] = 0
  
  if not solve_knights_tour_util(start_x, start_y, 1, board, move_x, move_y, N):
    print("Solution does not exist!")
  else:
    print_solution(board, N)
    
def solve_knights_tour_util(x, y, move_i, board, move_x, move_y, N):
  if move_i == N * N:
    return True
    
  for k in range(8):
    next_x = x + move_x[k]
    next_y = y + move_y[k]
    
    if is_valid(next_x, next_y, board, N):
      board[next_x][next_y] = move_i
      if solve_knights_tour_util(next_x, next_y, move_i + 1, board, move_x, move_y, N):
        return True
      board[next_x][next_y] = -1
  return False
if __name__ == "__main__":
  N = int(input("Enter the size of the chessboard (N x N): "))
  start_x = int(input(f"Enter the starting x-coordinate (0 to {N-1}):"))
  start_y = int(input(f"Enter the starting y-coordinate (0 to {N-1}):"))
  if 0 <= start_x < N and 0 <= start_y < N:
    solve_knights_tour(N, start_x, start_y)
  else:
    print("Invalid starting position!")
