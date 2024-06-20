from tabulate import tabulate

def gmKSfract(p, w, m):
    # Ensure that the profit list and weight list are of the same length
    assert len(p) == len(w), "p and w differ"

    # Get the number of items
    n = len(p)
    items = list(range(n))
    # Sort the items in descending order of their profit/weight ratio
    items.sort(key=lambda i: p[i] / w[i], reverse=True)

    total_weight = 0
    max_profit = 0

    # Initialize table data list
    table_data = []

    for i in items:
        # Check if adding the entire item exceeds the capacity
        if total_weight + w[i] <= m:
            total_weight += w[i]
            max_profit += p[i]
            # Append selected item's data to table data with fraction 1 indicating the entire item is selected
            table_data.append([i+1, p[i], w[i], 1.0])  
        else:
            # Calculate the remaining capacity
            remaining_weight = m - total_weight
            # Calculate the fraction of the item that can be added to the knapsack
            fraction = remaining_weight / w[i]
            # Update the profit and weight considering the fraction
            max_profit += p[i] * fraction
            # Append selected item's data to table data with the calculated fraction
            table_data.append([i+1, p[i], w[i], round(fraction, 2)])  

            # Break the loop as the knapsack is now full
            break

    # Print the items selected and their fractions (if any) in a tabular format
    print(tabulate(table_data, headers=['Item', 'Profit', 'Weight', 'Fraction'], tablefmt='grid'))
    
    # Print the maximum profit
    print(f"\nMaximum profit: {int(max_profit)}")

    # Return the maximum profit found (converted to integer)
    return int(max_profit)

# Function to run test cases automatically
def run_test_cases():
    # Test case 1: Basic example
    p1 = [60, 100, 120]
    w1 = [10, 20, 30]
    m1 = 50
    print("Test Case 1:")
    gmKSfract(p1, w1, m1)

    # Test case 2: All items can be selected
    p2 = [10, 20, 30]
    w2 = [1, 2, 3]
    m2 = 6
    print("\nTest Case 2:")
    gmKSfract(p2, w2, m2)

    # Test case 3: Fractional selection
    p3 = [10, 20, 30]
    w3 = [2, 3, 4]
    m3 = 5
    print("\nTest Case 3:")
    gmKSfract(p3, w3, m3)

    # Test case 4: Edge case with zero capacity
    p4 = [10, 20, 30]
    w4 = [1, 2, 3]
    m4 = 0
    print("\nTest Case 4:")
    gmKSfract(p4, w4, m4)

    # Uncomment the following test cases to use them in the future

    # Test case 5: High profit low weight items
    # p5 = [100, 200, 300]
    # w5 = [1, 2, 3]
    # m5 = 4
    # print("\nTest Case 5:")
    # gmKSfract(p5, w5, m5)

    # Test case 6: Low profit high weight items
    # p6 = [10, 20, 30]
    # w6 = [10, 20, 30]
    # m6 = 15
    # print("\nTest Case 6:")
    # gmKSfract(p6, w6, m6)

# Run the test cases
if __name__ == "__main__":
    run_test_cases()
