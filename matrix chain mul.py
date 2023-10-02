def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Create a 2D array to store the minimum number of scalar multiplications
    # dp[i][j] represents the minimum cost to multiply matrices from index i to j
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize the diagonal elements to 0 since multiplying a single matrix has no cost
    for i in range(n):
        dp[i][i] = 0
    
    # Chain length loop (l) starts from 2 to n
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                # Calculate the cost of multiplying matrices from i to k and k+1 to j
                cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # Reconstruct the optimal parenthesization
    def construct_parenthesization(i, j):
        if i == j:
            return f'M{str(i+1)}'  # Matrix is represented as M1, M2, M3, ...
        else:
            for k in range(i, j):
                if dp[i][j] == dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]:
                    left_parenthesis = construct_parenthesization(i, k)
                    right_parenthesis = construct_parenthesization(k+1, j)
                    return f'({left_parenthesis} x {right_parenthesis})'
    
    optimal_parenthesization = construct_parenthesization(0, n - 1)
    min_scalar_multiplications = dp[0][n - 1]
    
    return optimal_parenthesization, min_scalar_multiplications

# Example usage
matrices = [(2, 3), (3, 4), (4, 2)]
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)
print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)
