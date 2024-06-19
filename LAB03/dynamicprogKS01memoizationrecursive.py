from tabulate import tabulate

# Class to represent a node in the decision tree
class TreeNode:
    def __init__(self, n, W, profit, include=None):
        self.n = n  # The number of items being considered
        self.W = W  # The current capacity of the knapsack
        self.profit = profit  # The current profit at this node
        self.include = include  # Whether the current item is included (True/False)
        self.left = None  # Left child node (include the current item)
        self.right = None  # Right child node (exclude the current item)

# Function to solve the knapsack problem using memoization and build the decision tree
def knapsack(wt, val, W, n, root):
    # Base conditions: if there are no items or the capacity of the knapsack is 0, return 0
    if n == 0 or W == 0:
        return 0

    # Check if the result is already in the memoization table
    if t[n][W] != -1:
        return t[n][W]

    # If the weight of the nth item is less than or equal to the knapsack capacity W,
    # we have two options: include the nth item or exclude it
    if wt[n-1] <= W:
        # Create left child (include the item)
        root.left = TreeNode(n-1, W-wt[n-1], val[n-1], True)
        include_profit = val[n-1] + knapsack(wt, val, W-wt[n-1], n-1, root.left)
        # Create right child (exclude the item)
        root.right = TreeNode(n-1, W, 0, False)
        exclude_profit = knapsack(wt, val, W, n-1, root.right)
        # Store the maximum of including or excluding the item
        t[n][W] = max(include_profit, exclude_profit)
    else:
        # If the weight of the nth item is greater than the knapsack capacity W,
        # we cannot include the nth item in the knapsack
        root.right = TreeNode(n-1, W, 0, False)
        t[n][W] = knapsack(wt, val, W, n-1, root.right)
    
    # Return the value stored in the memoization table
    return t[n][W]

# Function to print the decision tree in a tree-like format
def print_tree(node, indent="", branch="Root"):
    if node is not None:
        print(f"{indent}└── {branch}: Item {node.n}, Capacity {node.W}, Profit {node.profit}, Include {node.include}")
        if node.left:
            print_tree(node.left, indent + "    ", "Left")
        if node.right:
            print_tree(node.right, indent + "    ", "Right")

# Main function to encapsulate the entire workflow
def main():
    # Input number of items
    n = int(input("Enter number of items: "))

    # Input the profits and weights of the items
    profit = []
    weight = []

    for i in range(n):
        p = int(input(f"Enter profit of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        profit.append(p)
        weight.append(w)

    # Input the capacity of the knapsack
    W = int(input("Enter capacity of knapsack: "))

    # Initialize the memoization table with -1 at first
    global t  # Declare t as global to be accessible inside knapsack function
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # Create the root node of the decision tree
    root = TreeNode(n, W, 0)

    # Calculate the maximum profit
    max_profit = knapsack(weight, profit, W, n, root)

    # Print the maximum profit
    print(f"\nMaximum profit: {max_profit}\n")

    # Print the decision tree
    print("Decision Tree:")
    print_tree(root)

# Call the main function to execute the program
if __name__ == '__main__':
    main()
