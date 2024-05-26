import math

# Input number of leaf nodes
n = int(input("Enter the number of leaf nodes: "))
# Calculate the depth of the tree
td = int(math.log(n, 2))

# Input leaf node values from right to left
print("Enter leaf node values from right to left")
l = []
for i in range(n):
    x = int(input(f'Enter {i+1} node value: '))
    l.append(x)

# Define initial values for alpha and beta
Mi, Ma = -1000, 1000

# Define the minimax function with alpha-beta pruning
def ab(cd, node_index, maxT, A, B, l):
    if cd == td:
        return l[node_index]
    
    if maxT:
        best = Mi
        for i in range(2):  # Two children: left and right
            val = ab(cd + 1, node_index * 2 + i, False, A, B, l)
            best = max(best, val)
            A = max(A, best)
            if B <= A:
                break
        return best
    else:
        best = Ma
        for i in range(2):  # Two children: left and right
            val = ab(cd + 1, node_index * 2 + i, True, A, B, l)
            best = min(best, val)
            B = min(B, best)
            if B <= A:
                break
        return best

# Call the function and print the result
result = ab(0, 0, True, Mi, Ma, l)
print(result)
