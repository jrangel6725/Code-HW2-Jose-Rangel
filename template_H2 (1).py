# Do not change the filename or function headers
# You are free to add helper functions
# note: you will only have 5 attempts to run the autograder

import numpy as np
import sys
from timeit import default_timer as timer
# import plot lib. to plot results.
# you may need to install matplotlib by typing "python3 -m pip install -U matplotlib" to test in your local machine
import matplotlib.pyplot as plt

# The required worst-case quick sort test has 1000 recursive calls.
sys.setrecursionlimit(10000)


# AI Tool Used: ChatGPT
# Interaction: I used ChatGPT to help me understand the algorithms when I
# struggled, especially with recursion, partitioning, and dynamic programming.
# Verification: I tested the code using the examples provided in the assignment
# and checked that the returned answers were correct.


# ============================================================================
# Q1. Quick sort
# ============================================================================
# function header for Q1.1 (Auto & manual grading)
# input_list -> list of integers
# return -> list of integers (ascending order)
#
# note: implement partition() and quick_sort() following the pseudocode in the lecture slides
# note: choose the pivot as the LAST element of the input array
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def partition(arr, low, high):
    # The last value is the pivot.
    pivot = arr[high]
    i = low - 1

    # Move values smaller than the pivot to the left side.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Put the pivot in its final position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(input_list):
    arr = list(input_list)

    def sort(low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)
    return arr


# function header for Q1.2 (Manual grading)
# note: no inputs and outputs are needed
# note: sort 1000 randomly generated integers with quick_sort and PRINT the running time
# note: this should have no errors
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_2():
    input_list = np.random.randint(0, 1000, 1000)
    ''' Hint: you can use "start = timer()" and "end = timer()", then "end - start" to get running time '''
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    start = timer()
    answer = quick_sort(input_list)
    end = timer()
    print("Random time:", end - start)
    return answer


# function header for Q1.3 (Manual grading)
# note: no inputs and outputs are needed
# note: sort 1000 integers in ASCENDING order with quick_sort and PRINT the running time
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_3():
    input_list = np.arange(0, 1000)
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    start = timer()
    answer = quick_sort(input_list)
    end = timer()
    print("Ascending time:", end - start)
    return answer


# function header for Q1.4 (Manual grading)
# note: no inputs and outputs are needed
# note: sort 1000 integers in DESCENDING order with quick_sort and PRINT the running time
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_4():
    input_list = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    start = timer()
    answer = quick_sort(input_list)
    end = timer()
    print("Descending time:", end - start)
    return answer


# Q1.5 (Manual grading)
# Explain why the running time of Q1.3 and Q1.4 is greater than the running time of Q1.2.
# Write your explanation below as a Python comment
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
#
# {write your answer here...}
# Q1.3 and Q1.4 take longer because the last element is a bad pivot for an
# already sorted list. The partitions become very unbalanced, which gives
# quick sort O(n^2) time instead of its average O(n log n) time.
#


# function header for Q1.6 (Auto & manual grading)
# input_list -> list of integers
# return -> list of integers (ascending order)
#
# note: modify the quick sort algorithm (modified_partition / modified_quick_sort)
#       so that the ascending and descending cases run faster
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def modified_partition(arr, low, high):
    # Use the middle value instead of always using the last value.
    middle = (low + high) // 2
    arr[middle], arr[high] = arr[high], arr[middle]
    return partition(arr, low, high)


def modified_quick_sort(input_list):
    arr = list(input_list)

    def sort(low, high):
        if low < high:
            pivot_index = modified_partition(arr, low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)
    return arr


# function header for Q1.6 (Manual grading)
# note: no inputs and outputs are needed
# note: PRINT the running time of modified_quick_sort for input_A and input_B
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_6():
    input_A = np.arange(0, 1000)
    input_B = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    start = timer()
    modified_quick_sort(input_A)
    end = timer()
    print("Modified ascending time:", end - start)

    start = timer()
    modified_quick_sort(input_B)
    end = timer()
    print("Modified descending time:", end - start)


# ============================================================================
# Q2. Heap sort
# ============================================================================
# function header for Q2 (Auto & manual grading)
# input_list -> list of integers (unordered)
# return -> list of integers sorted in DESCENDING order
#
# Ex: input_list = [-31, 53, 84, 62, -32, -97, -19, 6, 33, 28, -7, 54, 53, 2, -27, 36, 21, 37, -90]
#
# note: implement heap_sort using heapify() and build_heap() helper functions
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def heapify(arr, size, root):
    # This version makes a min heap.
    smallest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < size and arr[left] < arr[smallest]:
        smallest = left
    if right < size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != root:
        arr[root], arr[smallest] = arr[smallest], arr[root]
        heapify(arr, size, smallest)


def build_heap(arr):
    # Start with the last parent node and work toward the root.
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)


def heap_sort(input_list):
    arr = list(input_list)
    build_heap(arr)

    # Put the smallest values at the end to get descending order.
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)

    return arr


# ============================================================================
# Q3. Red-white-blue (stable) sorting of a 2-D array
# ============================================================================
# function header for Q3 (Auto & manual grading)
# input_list -> 2D integer array, ex) [[6, 0], [212, 1], [247, 0], [352, 1], [388, 1]]
# return -> 2D array sorted in the order of red(0), white(1), then blue(2)
#
# note: the color is stored in the second column, arr[i][1]: 0 = red, 1 = white, 2 = blue
# note: the ORIGINAL order of objects with the same color must be preserved (stable)
# note: Do not use any Python built-in sorting functions
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def color_sort(input_list):
    red = []
    white = []
    blue = []

    # Adding items to separate lists keeps equal-color items stable.
    for item in input_list:
        if item[1] == 0:
            red.append(list(item))
        elif item[1] == 1:
            white.append(list(item))
        else:
            blue.append(list(item))

    return red + white + blue


# ============================================================================
# Q4. Max-Min problem (divide and conquer)
# ============================================================================
# function header for Q4 (Auto & manual grading)
# input_list -> list of integers, ex) [-100, 10, 5, 6, -62, 23, 14]
# return -> min and max value of the array as a list, ex) [-100, 23]
#
# note: use the divide-and-conquer approach
# note: Do not use any Python built-in sorting functions
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def max_min(input_list):
    def find_values(left, right):
        if left == right:
            return [input_list[left], input_list[left]]

        if right == left + 1:
            if input_list[left] < input_list[right]:
                return [input_list[left], input_list[right]]
            return [input_list[right], input_list[left]]

        # Divide the list into two smaller problems.
        middle = (left + right) // 2
        first = find_values(left, middle)
        second = find_values(middle + 1, right)

        minimum = min(first[0], second[0])
        maximum = max(first[1], second[1])
        return [minimum, maximum]

    if len(input_list) == 0:
        return []
    return find_values(0, len(input_list) - 1)


# ============================================================================
# Q5. Subset sum (Dynamic Programming)
# ============================================================================
# function header for Q5 (Auto & manual grading)
# input_set -> list of non-negative integers
# target_sum -> integer target value
# return -> True or False
#
# Ex: input_set = [3, 2, 10, 4, 8, 9], target_sum = 12 -> True
#
# note: use a DP approach (either top-down or bottom-up)
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def subset_sum(input_set, target_sum):
    possible = [False] * (target_sum + 1)
    possible[0] = True

    for value in input_set:
        # Go backward so one value is not used more than once.
        for total in range(target_sum, value - 1, -1):
            if possible[total - value]:
                possible[total] = True

    return possible[target_sum]


# ============================================================================
# Q6. Minimum cost path in a 2-D cost matrix
# ============================================================================
# From a cell (i, j) only the cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed.
# minCost(M, N) = min( minCost(M-1, N-1), minCost(M-1, N), minCost(M, N-1) ) + cost[M][N]
#
# function header for Q6.1 (Auto & manual grading)
# costs -> list of lists (2D array)
# m_minus_one, n_minus_one -> integers (M-1 and N-1)
# return -> integer (minimum cost)
#
# note: use a NAIVE RECURSIVE approach (not DP); also PRINT its running time
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_recursive(costs, m_minus_one, n_minus_one):
    if m_minus_one == 0 and n_minus_one == 0:
        return costs[0][0]

    if m_minus_one == 0:
        return costs[0][n_minus_one] + min_cost_path_recursive(
            costs, 0, n_minus_one - 1)

    if n_minus_one == 0:
        return costs[m_minus_one][0] + min_cost_path_recursive(
            costs, m_minus_one - 1, 0)

    diagonal = min_cost_path_recursive(
        costs, m_minus_one - 1, n_minus_one - 1)
    up = min_cost_path_recursive(costs, m_minus_one - 1, n_minus_one)
    left = min_cost_path_recursive(costs, m_minus_one, n_minus_one - 1)

    return costs[m_minus_one][n_minus_one] + min(diagonal, up, left)


# function header for Q6.2 (Auto & manual grading)
# costs -> list of lists (2D array)
# m_minus_one, n_minus_one -> integers (M-1 and N-1)
# return -> integer (minimum cost)
#
# note: use the TOP-DOWN DP approach (memoization); also PRINT its running time
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_topdown(costs, m_minus_one, n_minus_one):
    memo = {}

    def find_cost(row, column):
        if (row, column) in memo:
            return memo[(row, column)]

        if row == 0 and column == 0:
            return costs[0][0]

        if row == 0:
            answer = costs[row][column] + find_cost(row, column - 1)
        elif column == 0:
            answer = costs[row][column] + find_cost(row - 1, column)
        else:
            answer = costs[row][column] + min(
                find_cost(row - 1, column - 1),
                find_cost(row - 1, column),
                find_cost(row, column - 1))

        memo[(row, column)] = answer
        return answer

    return find_cost(m_minus_one, n_minus_one)


# function header for Q6.3 (Auto & manual grading)
# costs -> list of lists (2D array)
# m_minus_one, n_minus_one -> integers (M-1 and N-1)
# return -> integer (minimum cost)
#
# note: use the BOTTOM-UP DP approach; also PRINT its running time
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_bottomup(costs, m_minus_one, n_minus_one):
    rows = m_minus_one + 1
    columns = n_minus_one + 1
    dp = [[0] * columns for _ in range(rows)]

    dp[0][0] = costs[0][0]

    # Fill the first row and first column.
    for column in range(1, columns):
        dp[0][column] = dp[0][column - 1] + costs[0][column]
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + costs[row][0]

    # Fill the rest of the table.
    for row in range(1, rows):
        for column in range(1, columns):
            dp[row][column] = costs[row][column] + min(
                dp[row - 1][column - 1],
                dp[row - 1][column],
                dp[row][column - 1])

    return dp[m_minus_one][n_minus_one]


# function header for Q6.4 (Manual grading, 0 points autograder)
# costs -> list of lists (2D array)
# m_minus_one, n_minus_one -> integers (M-1 and N-1)
# return -> N/C (the PRINTED path is graded manually)
#
# note: find and PRINT the minimum cost path, e.g., (0,0)->(0,1)->......->(9,9)
# note: re-use your min_cost_path_bottomup implementation inside this wrapper
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_wrapper(costs, m_minus_one, n_minus_one):
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    answer = min_cost_path_bottomup(costs, m_minus_one, n_minus_one)
    rows = m_minus_one + 1
    columns = n_minus_one + 1
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = costs[0][0]

    for column in range(1, columns):
        dp[0][column] = dp[0][column - 1] + costs[0][column]
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + costs[row][0]
    for row in range(1, rows):
        for column in range(1, columns):
            dp[row][column] = costs[row][column] + min(
                dp[row - 1][column - 1],
                dp[row - 1][column],
                dp[row][column - 1])

    row = m_minus_one
    column = n_minus_one
    path = [(row, column)]

    # Trace the path backward using the smallest previous DP value.
    while row != 0 or column != 0:
        choices = []
        if row > 0 and column > 0:
            choices.append((dp[row - 1][column - 1], row - 1, column - 1))
        if row > 0:
            choices.append((dp[row - 1][column], row - 1, column))
        if column > 0:
            choices.append((dp[row][column - 1], row, column - 1))

        best = min(choices)
        row, column = best[1], best[2]
        path.append((row, column))

    path.reverse()
    print("Minimum cost:", answer)
    print("Path:", "->".join("(" + str(x) + "," + str(y) + ")"
                              for x, y in path))


# ============================================================================
# Q7. Matrix-chain multiplication minimization
# ============================================================================
# m[i, j] = 0                                                                  if i == j
#         = min over i <= k < j of ( m[i,k] + m[k+1,j] + q[i-1]*q[k]*q[j] )    if i < j
#
# function header for Q7.1 (Auto & manual grading)
# q -> list of matrix dimensions
# i, j -> integers
# return -> integer (minimum number of scalar multiplications)
#
# Ex: q = [9, 46, 4, 18, 21, 40, 19, 25, 14, 37, 33], i = 1, j = 10 -> 21012
#
# note: use the TOP-DOWN DP approach
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_topdown(q, i, j):
    memo = {}

    def find_cost(left, right):
        if left == right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        best = float("inf")
        for k in range(left, right):
            current = (find_cost(left, k) +
                       find_cost(k + 1, right) +
                       q[left - 1] * q[k] * q[right])
            if current < best:
                best = current

        memo[(left, right)] = best
        return best

    return find_cost(i, j)


# function header for Q7.2 (Auto & manual grading)
# q -> list of matrix dimensions
# return -> tuple of 2 lists: the solution matrix m, and the parenthesis-location matrix s
#
# note: use the BOTTOM-UP DP approach
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_bottomup(q):
    number = len(q) - 1
    m = [[0] * (number + 1) for _ in range(number + 1)]
    s = [[0] * (number + 1) for _ in range(number + 1)]

    # length is the number of matrices in the current chain.
    for length in range(2, number + 1):
        for i in range(1, number - length + 2):
            j = i + length - 1
            m[i][j] = float("inf")

            for k in range(i, j):
                current = (m[i][k] + m[k + 1][j] +
                           q[i - 1] * q[k] * q[j])
                if current < m[i][j]:
                    m[i][j] = current
                    s[i][j] = k

    return m, s


# function header for Q7.3 (Auto & manual grading)
# q -> list of matrix dimensions
# matrix -> list of matrix names, ex) ['A1', 'A2', ..., 'A10']
# return -> string of the full optimal parenthesization, ex) "((A1A2A3)(A4A5))"
#
# note: use parentheses '(' and ')' instead of '{' and '}'
# note: enclose the outermost part with parentheses, and use NO spaces between characters
# note: re-use your matrix_chain_bottomup implementation inside this wrapper
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_parenthesization(q, matrix):
    m, s = matrix_chain_bottomup(q)

    def make_string(i, j):
        if i == j:
            return matrix[i - 1]
        k = s[i][j]
        return "(" + make_string(i, k) + make_string(k + 1, j) + ")"

    return make_string(1, len(matrix))


# ============================================================================
# Q8. Coin change - feasibility (Dynamic Programming)
# ============================================================================
# Given an unlimited supply of coins of denominations x1, x2, ..., xn, decide whether
# it is possible to make change for a value V. Target time complexity: O(n * V).
#
# Ex: coins = [5, 10], V = 15 -> True ; V = 20 -> True ; V = 12 -> False
#
# function header for Q8.1 (Manual grading)
# note: no inputs and outputs are needed
# note: describe (1) the optimal structure, (2) the overlapping subproblems,
#       and (3) the recurrence equation of the problem
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q8_1():
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    # A value can be made if value - coin can be made first.
    # The smaller values repeat, so the results can be stored in a table.
    # possible[0] = True
    # possible[value] = OR(possible[value - coin]) for every valid coin.
    pass


# function header for Q8.2 (Manual grading)
# coins -> list of integer denominations
# target_value -> integer value V
# return -> True or False
#
# note: implement a BOTTOM-UP DP algorithm following your recurrence from Q8.1
# note: explain its time complexity as a comment
# note: write comments for key lines of code (for, while, if, ...) to demonstrate your comprehension
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
#
def coin_change_dp(coins, target_value):
    possible = [False] * (target_value + 1)
    possible[0] = True

    for value in range(1, target_value + 1):
        for coin in coins:
            if coin <= value and possible[value - coin]:
                possible[value] = True
                break

    return possible[target_value]
# Time complexity: {write your answer here...}
# Time complexity is O(n * V), where n is the number of coins and V is the target.


# function header for Q8.3 (Manual grading)
# coins -> list of integer denominations
# target_value -> integer value V
# return -> True or False
#
# note: implement a NAIVE RECURSIVE algorithm for the same problem
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def coin_change_recursive(coins, target_value):
    def solve(value, index):
        if value == 0:
            return True
        if index == len(coins):
            return False

        # Try using the current coin again.
        if coins[index] <= value and coins[index] > 0:
            if solve(value - coins[index], index):
                return True

        # Try skipping the current coin.
        return solve(value, index + 1)

    return solve(target_value, 0)


# function header for Q8.3 (Manual grading)
# note: no inputs and outputs are needed
# note: compare the running time of coin_change_dp and coin_change_recursive and PRINT the results
# note: state whether your DP solution performs better, as a comment
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q8_3():
    coins = [5, 10, 1, 25]
    target_value = 100
    ''' Hint: you can use "start = timer()" and "end = timer()", then "end - start" to get running time '''
    ''' write your answers (codes/texts) from here '''


    ''' end your answers '''
    start = timer()
    dp_answer = coin_change_dp(coins, target_value)
    dp_time = timer() - start

    start = timer()
    recursive_answer = coin_change_recursive(coins, target_value)
    recursive_time = timer() - start

    print("DP answer:", dp_answer)
    print("DP time:", dp_time)
    print("Recursive answer:", recursive_answer)
    print("Recursive time:", recursive_time)

    # DP is usually faster because it does not repeat the same subproblems.


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope

    # Examples:
    # print(quick_sort([5, 2, 4, 1, 3]))
    # q1_2(); q1_3(); q1_4(); q1_6()
    # print(modified_quick_sort([5, 2, 4, 1, 3]))
    # print(heap_sort([-31, 53, 84, 62, -32, -97, -19, 6, 33, 28]))
    # print(color_sort([[6, 0], [212, 1], [247, 0], [352, 1], [388, 1]]))
    # print(max_min([-100, 10, 5, 6, -62, 23, 14]))
    # print(subset_sum([3, 2, 10, 4, 8, 9], 12))
    # cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    # print(min_cost_path_recursive(cost, 2, 2))
    # print(min_cost_path_topdown(cost, 2, 2))
    # print(min_cost_path_bottomup(cost, 2, 2))
    # min_cost_path_wrapper(cost, 2, 2)
    # q = [9, 46, 4, 18, 21, 40, 19, 25, 14, 37, 33]
    # print(matrix_chain_topdown(q, 1, 10)); print(matrix_chain_bottomup(q))
    # print(matrix_chain_parenthesization(q, ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']))
    # print(coin_change_dp([5, 10], 15)); print(coin_change_recursive([5, 10], 12)); q8_3()
    pass
