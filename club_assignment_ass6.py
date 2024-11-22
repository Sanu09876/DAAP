def get_cost_matrix():
    N = int(input("Enter the number of students / clubs (N): "))
    print("Enter the cost of the matrix (N X N) row by row, each separated by space:")
    cost_matrix = []
    for i in range(N):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        cost_matrix.append(row)
    return cost_matrix
  
def is_valid_assignment(student, club, current_assignment):
    return club not in current_assignment

def assign_clubs(student, current_cost, current_assignment, cost_matrix, N):
    global min_cost, optimal_assignment
    if student == N:  # Base case: all students have been assigned to clubs
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_assignment = current_assignment.copy()  # Save the optimal assignment
        return

    for club in range(N):
        if is_valid_assignment(student, club, current_assignment):
            current_assignment[student] = club  # Assign student to this club
            new_cost = current_cost + cost_matrix[student][club]
            if new_cost < min_cost:  # Only recurse if there's a potential to improve cost
                assign_clubs(student + 1, new_cost, current_assignment, cost_matrix, N)
            current_assignment[student] = -1  # Reset assignment for this student

def solve_club_assignment():
    global min_cost, optimal_assignment
    cost_matrix = get_cost_matrix()
    N = len(cost_matrix)
    min_cost = float('inf')  # Initialize with a large value
    optimal_assignment = [-1] * N  # Initialize the assignment to -1 (unassigned)
    current_assignment = [-1] * N  # Initialize the current assignment

    assign_clubs(0, 0, current_assignment, cost_matrix, N)

    # Output the result
    print("Minimum Assignment Cost:", min_cost)
    print("Optimal Assignment (Student to Club):", [x + 1 for x in optimal_assignment])  # Convert 0-indexed to 1-indexed

# Start the club assignment problem
solve_club_assignment()

