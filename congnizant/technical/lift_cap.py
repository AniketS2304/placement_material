# 2. Lift Capacity Problem
# Problem Statement
# There is a lift in your society that can accommodate a maximum weight of 
# X
# X units. The weights of people planning to use the lift are given in an integer array 
# A
# A of size 
# N
# N.
# Your task is to return the maximum number of people that can use the lift together without exceeding its weight capacity.

# Input
# int N: Number of people.

# int X: Maximum weight capacity of the lift.

# int[] A: Array containing the weights of the people.

# Output
# Return an integer representing the maximum number of people that can use the lift together.

# Example 1
# text
# Input:
# N = 3
# X = 9
# A = [5, 1, 5]

# Output:
# 2

# Explanation:
# The two people of weights 1 and 5 can together use the lift (1+5=6 < 9).



def longestsubarray(arr,x):
    n = len(arr)
    
    max_  = 0
    
    l=0
    sum_= 0
    for r in range(n):
        sum_ += arr[r]
        
        while sum_ > x:
            sum_ -= arr[l]
            l+=1
        max_  = max(max_ , r-l+1)
    
    return max_


N = 3
X = 9
A = [5, 1, 5]

print(longestsubarray(A,X))