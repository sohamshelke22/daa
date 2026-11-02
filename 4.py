# 0-1 Knapsack Problem using Dynamic Programming (with selected items)

def knapsack(weights, values, capacity):
    n = len(values)
    
    # Step 1: Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Step 2: Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Step 3: Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)  # item i was included
            w -= weights[i-1]

    selected_items.reverse()  # To show items in original order

    # Step 4: Return results
    return dp[n][capacity], selected_items


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)
print("Items included (1-indexed) =", items)















def knapsack(w, p, c):
    n = len(w)
    dp = [[0] * (c + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(p[i - 1] + dp[i - 1][j - w[i - 1]],
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print("Maximum Profit:", dp[n][c])

w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))
c = int(input("Enter capacity: "))

knapsack(w, p, c)

'''
Read , lines 1 to 200
Completed with input: {
  "path": "C:\\Users\\anujg\\OneDrive\\Desktop\\MESWCOE\\Seventh Semester\\LP3\\DAA\\4.py",
  "view_range": [
    1,
    200
  ]
}

Requested chat rename
Completed with input: {
  "title": "0/1 Knapsack I/O",
  "automatic": true
}

Sample input:
Enter weights: 10 20 30
Enter profits: 60 100 120
Enter capacity: 50

Sample output:
Maximum Profit: 220

Explanation:
This is 0/1 Knapsack, so each item can be taken only once.

- Item 1: weight 10, profit 60
- Item 2: weight 20, profit 100
- Item 3: weight 30, profit 120
- Capacity = 50

Best combination:
- 20 + 30 = 50
- Profit = 100 + 120 = 220

So the output is:
Maximum Profit: 220

Another example:
Input:
Enter weights: 5 10 15
Enter profits: 10 20 30
Enter capacity: 15

Output:
Maximum Profit: 30

Because the best choice is the item with weight 15 and profit 30.
'''