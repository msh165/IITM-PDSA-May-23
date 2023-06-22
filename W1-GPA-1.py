# Write a function Find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.
# Note - The list can contain more than one subset of p elements that have the same minimum difference value.
# Example
# Let L = [3, 4, 1, 9, 56, 7, 9, 12, 13] and P = 5
# If we see the following two subsets of 5 elements from L
# [3, 4, 7, 9, 9] or [7, 9, 9, 12, 13]
# Here, the difference between the maximum value and the minimum value in both subset is 9-3
# = 6 or 13 - 7 = 6 which is minimum. So the output will be 6.
# Sample Input
# [3, 4, 1, 9, 56, 7, 9, 12]
# 5
# Output
# 6

def find_Min_Difference(l,p):
    min_diff=10000
    combinations = itertools.combinations(l, p)
    for combo in combinations:
        max_num = max(combo)
        min_num = min(combo)
        diff = max_num-min_num
        if diff<min_diff:
            min_diff=diff
    return min_diff
