from tabulate import tabulate

# Function to solve the knapsack problem using tabulation
def knapsack(wt, val, W, n):
    # Create a 2D array to store the maximum profit for each subproblem
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the dp array in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                # Include the item and check for maximum value
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]

    # The last cell of dp array contains the maximum profit for the given capacity W
    return dp, dp[n][W]

# Main function to encapsulate the entire workflow
def main():
    # Input number of items
    n = int(input("Enter number of items: "))

    # Input the profits and weights of the items
    profit = []
    weight = []

    for i in range(n):
        p = int(input(f"Enter profit of item {i + 1}: "))
        w = int(input(f"Enter weight of item {i + 1}: "))
        profit.append(p)
        weight.append(w)

    # Input the capacity of the knapsack
    W = int(input("Enter capacity of knapsack: "))

    # Calculate the maximum profit and the dp table
    dp, max_profit = knapsack(weight, profit, W, n)

    # Print the maximum profit
    print(f"Maximum profit: {max_profit}")

    # Visualize the table
    print("\nDP Table:")
    table = [[f"{cell}" for cell in row] for row in dp]
    headers = [f"W{i}" for i in range(W + 1)]
    table_display = tabulate(table, headers, showindex="always", tablefmt="grid")

    # Split the table into lines and print to fit screen width
    for line in table_display.split("\n"):
        print(line[:150])  # Adjust the number of characters to fit the screen if needed

# Call the main function to execute the program
if __name__ == '__main__':
    main()
