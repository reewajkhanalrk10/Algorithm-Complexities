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
    print("\nMaximum profit is:", gmKSfract(p, w, m))
