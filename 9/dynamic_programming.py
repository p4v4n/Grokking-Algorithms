# Dynamic Programming

# 1) Dynamic programming is useful when you’re trying to optimize something given a constraint.
# 2) You can use dynamic programming when the problem can be broken into discrete subproblems.
# 3) Every dynamic-programming solution involves a grid.

"""
# Knapsack Problem:

cell[i][j] = max(cell[i-1][j-i], (current_item_value + cell[i-1][j-(current_item_weight)]))

# Longest Common Sub-String:

if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1] + 1
else:
    cell[i][j] = 0

# Longest Common Sub-Sequence:

if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1] + 1
else:
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
"""
#----------------
#Exercise:Draw and fill in the grid to calculate the longest common substring between blue and clues.


def longest_common_substring(word_a, word_b):
    m, n = len(word_a), len(word_b)
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word_a[i-1] == word_b[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = 0
    max_substring_value = max([max(li) for li in grid])
    return max_substring_value

print(longest_common_substring("blue","clues"))