rows = int(input("Enter the number of rows: "))
colmns = int(input("Enter the number of columns: "))

initial_matrix = []
print("\nInitial matrix:")
for i in range(rows):
    row = []
    for j in range(colmns):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    initial_matrix.append(row)
    
goal_matrix = []
print("\nGoal matrix: ")
for i in range(rows):
    row1 = []
    for j in range(colmns):
        element1 = int(input(f"Enter element at position ({i},{j}): "))
        row1.append(element1)
    goal_matrix.append(row1)

def zero_position(matrix):
    for i in range(rows):
        for j in range(colmns):
            if matrix[i][j] == 0:
                return (i,j)
    return (-1,-1)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def moves(matrix, choice):
    x, y = zero_position(matrix)
    if choice == 'up' and x > 0:
        matrix[x][y], matrix[x-1][y] = matrix[x-1][y], matrix[x][y]
    elif choice == 'down' and x < rows-1:
        matrix[x][y], matrix[x+1][y] = matrix[x+1][y], matrix[x][y]
    elif choice == 'left' and y > 0:
        matrix[x][y], matrix[x][y-1] = matrix[x][y-1], matrix[x][y]
    elif choice == 'right' and y < colmns-1:
        matrix[x][y], matrix[x][y+1] = matrix[x][y+1], matrix[x][y]
    print_matrix(matrix)

def out_of_order(matrix1, matrix2):
    count = 0
    for i in range(rows):
        for j in range(colmns):
            if matrix1[i][j] != matrix2[i][j]:
                count += 1
    print(f"\nNumber of out of order elements: {count}")
    return count

def main():
    print("\nOriginal matrix")
    print_matrix(initial_matrix)
    print("\nGoal matrix")
    print_matrix(goal_matrix)
    order1 = out_of_order(initial_matrix, goal_matrix)
    if initial_matrix == goal_matrix:
        print("Congratulations! You've reached the goal matrix.")
    else:
        while True:
            choice = input("\nEnter your choice (up, down, left, right): ")
            if choice in ['up', 'down', 'left', 'right']:
                moves(initial_matrix, choice)
                order2 = out_of_order(initial_matrix, goal_matrix)
                if order2 > order1:
                    print("Invalid move!")
                    break
                order1 = order2
                if initial_matrix == goal_matrix:
                    print("Congratulations! You've reached the goal matrix.")
                    break  
            else:
                print("Invalid choice!")
                continue
            
if __name__ == "__main__":
    main()