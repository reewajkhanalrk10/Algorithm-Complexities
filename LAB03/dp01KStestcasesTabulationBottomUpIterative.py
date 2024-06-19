import pandas as pd

# Function to solve the knapsack problem using Tabulation (Bottom-Up) approach
def knapsack_tabulation(wt, val, W, n):
    # Initialize a table to store results of subproblems
    t = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                t[i][w] = 0
            elif wt[i - 1] <= w:
                t[i][w] = max(val[i - 1] + t[i - 1][w - wt[i - 1]], t[i - 1][w])
            else:
                t[i][w] = t[i - 1][w]

    return t[n][W], t

# Function to print the memoization table in tabular format using pandas
def print_tabulation_table(table, n, W):
    df = pd.DataFrame(table)
    df.index = ["Item " + str(i) for i in range(n + 1)]
    df.columns = ["W" + str(i) for i in range(W + 1)]
    print("\nMemoization Table:")
    print(df)

# Function to run test cases
def run_test_cases():
    # Test case 1: Basic example
    profit1 = [60, 100, 120]
    weight1 = [10, 20, 30]
    W1 = 50
    n1 = len(profit1)
    max_profit1, memoization_table1 = knapsack_tabulation(weight1, profit1, W1, n1)
    print(f"\nTest Case 1: Maximum profit = {max_profit1}")
    print_tabulation_table(memoization_table1, n1, W1)

    # # Test case 2: Edge case with zero capacity
    # profit2 = [10, 20, 30]
    # weight2 = [1, 2, 3]
    # W2 = 0
    # n2 = len(profit2)
    # max_profit2, memoization_table2 = knapsack_tabulation(weight2, profit2, W2, n2)
    # print(f"\nTest Case 2: Maximum profit = {max_profit2}")
    # print_tabulation_table(memoization_table2, n2, W2)

    # # Test case 3: All items have zero profit
    # profit3 = [0, 0, 0]
    # weight3 = [10, 20, 30]
    # W3 = 50
    # n3 = len(profit3)
    # max_profit3, memoization_table3 = knapsack_tabulation(weight3, profit3, W3, n3)
    # print(f"\nTest Case 3: Maximum profit = {max_profit3}")
    # print_tabulation_table(memoization_table3, n3, W3)

# Run the test cases
if __name__ == "__main__":
    run_test_cases()
