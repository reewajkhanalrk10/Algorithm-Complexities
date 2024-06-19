from tabulate import tabulate

def bfmKS01(p, w, m):
    # Ensure that the profit list and weight list are of the same length
    assert len(p) == len(w), "p and w differ"

    # Get the number of items
    n = len(p)
    # Initialize the maximum profit to 0
    max_profit = 0
    # Set the total weight limit to m
    total_weight = m
    # Initialize the solution string to an empty string
    soln = ''
    
    # Initialize table data list
    table_data = []
    
    # Iterate through all possible combinations of items
    for i in range(2**n):
        # Convert the current combination number to a binary string
        s = bin(i)[2:].rjust(n, '0')
        # Calculate the total profit for the current combination
        profit = sum((int(s[j])) * p[j] for j in range(n))
        # Calculate the total weight for the current combination
        weight = sum((int(s[j])) * w[j] for j in range(n))

        # Append combination, profit, and weight to table data
        table_data.append([s, profit, weight])
    
        # If the current combination's profit is greater than the max profit
        # and its weight is within the allowed limit, update the max profit and solution
        if profit > max_profit and weight <= total_weight:
            max_profit = profit
            soln = s

    # Print the combinations, profits, and weights in a tabular format
    print(tabulate(table_data, headers=['Combination', 'Profit', 'Weight'], tablefmt='grid'))
    
    # Print the best combination and the maximum profit
    print(f"\nBest combination: {soln}")
    print(f"Maximum profit: {max_profit}")

    # Return the maximum profit found
    return max_profit

# Example usage
if __name__ == "__main__":
    # Input number of items
    n = int(input("Enter number of items: "))

    # Input profits
    p = []
    for i in range(n):
        profit = int(input(f"Enter profit for item {i+1}: "))
        p.append(profit)

    # Input weights
    w = []
    for i in range(n):
        weight = int(input(f"Enter weight for item {i+1}: "))
        w.append(weight)

    # Input maximum weight
    m = int(input("Enter maximum weight capacity: "))

    # Call the function with the user-provided parameters and print the result
    print("\nMaximum profit is:", bfmKS01(p, w, m))
