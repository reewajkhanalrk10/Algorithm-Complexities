from tabulate import tabulate

def bfmKSfract(p, w, m):
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
        # Initialize profit and weight to 0
        profit = 0
        weight = 0
        # Calculate profit and weight for the current combination
        for j in range(n):
            if s[j] == '1':
                profit += p[j]
                weight += w[j]
            elif s[j] == '0':
                pass
        
        # Calculate fractional weight for '0' elements in s
        if weight > total_weight:
            continue
        fraction = (total_weight - weight) / sum(w[j] for j in range(n) if s[j] == '0')
        profit += fraction * sum(p[j] for j in range(n) if s[j] == '0')
        weight += fraction * sum(w[j] for j in range(n) if s[j] == '0')
        
        # Append combination, profit, and weight to table data
        table_data.append([s, profit, weight])

        # Update maximum profit and solution if the current combination yields higher profit
        if profit > max_profit:
            max_profit = profit
            soln = s

    # Print the combinations, profits, and weights in a tabular format
    print(tabulate(table_data, headers=['Combination', 'Profit', 'Weight'], tablefmt='grid'))
    
    # Print the best combination and the maximum profit
    print(f"\nBest combination: {soln}")
    print(f"Maximum profit: {int(max_profit)}")

    # Return the maximum profit found (converted to integer)
    return int(max_profit)

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
    print("\nMaximum profit is:", bfmKSfract(p, w, m))
