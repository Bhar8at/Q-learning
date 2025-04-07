
# Initializing the structure
def matrix(x):
    return [[" 0 " for i in range(x)] for i in range(x)]


# UI related functions
def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

def space():
    print("\n"*5)