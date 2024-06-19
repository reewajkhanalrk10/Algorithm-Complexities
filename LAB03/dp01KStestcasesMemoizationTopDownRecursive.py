#MemoizationTopDownRecursive
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

# Function to run test cases
def run_test_cases():
    # Test case 1: Example from textbooks or online tutorials
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)

    global t
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    root = TreeNode(n, W, 0)
    max_profit = knapsack(weight, profit, W, n, root)

    print(f"\nTest Case 1: Maximum profit = {max_profit}\n")
    print("Decision Tree:")
    print_tree(root)

    # # Test case 2: Custom scenario with different values
    # profit = [70, 20, 39, 100, 50]
    # weight = [31, 10, 20, 40, 50]
    # W = 100
    # n = len(profit)

    # t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # root = TreeNode(n, W, 0)
    # max_profit = knapsack(weight, profit, W, n, root)

    # print(f"\nTest Case 2: Maximum profit = {max_profit}\n")
    # print("Decision Tree:")
    # print_tree(root)

    # # Test case 3: Edge case with very small capacity and weights
    # profit = [10, 20, 30]
    # weight = [1, 2, 3]
    # W = 2
    # n = len(profit)

    # t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # root = TreeNode(n, W, 0)
    # max_profit = knapsack(weight, profit, W, n, root)

    # print(f"\nTest Case 3: Maximum profit = {max_profit}\n")
    # print("Decision Tree:")
    # print_tree(root)

if __name__ == '__main__':
    run_test_cases()
