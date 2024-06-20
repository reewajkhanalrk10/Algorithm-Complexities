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
        
        # Calculate fractional weight for '0' elements in s
        if weight > total_weight:
            continue
        
        remaining_weight = total_weight - weight
        if remaining_weight > 0:
            total_zero_weight = sum(w[j] for j in range(n) if s[j] == '0')
            if total_zero_weight > 0:
                fraction = remaining_weight / total_zero_weight
                profit += fraction * sum(p[j] for j in range(n) if s[j] == '0')
                weight += fraction * total_zero_weight
        
        # Append combination, profit, and weight to table data
        table_data.append([s, round(profit, 2), round(weight, 2)])

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

# Function to run test cases automatically
def run_test_cases():
    # Test case 1: Basic example
    p1 = [60, 100, 120]
    w1 = [10, 20, 30]
    m1 = 50
    print("Test Case 1:")
    bfmKSfract(p1, w1, m1)

    # Test case 2: All items can be selected
    p2 = [10, 20, 30]
    w2 = [1, 2, 3]
    m2 = 6
    print("\nTest Case 2:")
    bfmKSfract(p2, w2, m2)

    # Test case 3: Fractional selection (similar behavior to test edge case)
    p3 = [10, 20, 30]
    w3 = [2, 3, 4]
    m3 = 5
    print("\nTest Case 3:")
    bfmKSfract(p3, w3, m3)

    # Test case 4: Edge case with zero capacity
    p4 = [10, 20, 30]
    w4 = [1, 2, 3]
    m4 = 0
    print("\nTest Case 4:")
    bfmKSfract(p4, w4, m4)

    # Uncomment the following test cases to use them in the future

    # Test case 5: High profit low weight items
    # p5 = [100, 200, 300]
    # w5 = [1, 2, 3]
    # m5 = 4
    # print("\nTest Case 5:")
    # bfmKSfract(p5, w5, m5)

    # Test case 6: Low profit high weight items
    # p6 = [10, 20, 30]
    # w6 = [10, 20, 30]
    # m6 = 15
    # print("\nTest Case 6:")
    # bfmKSfract(p6, w6, m6)

# Run the test cases
if __name__ == "__main__":
    run_test_cases()
