# 1. Count Special Subarrays of Size 3
# Problem Statement
# You are given an array of integers containing 
# N
# N elements. Your task is to find and return the total number of subarrays of size 3 such that the sum of the first element and the third element is equal to the second element.

# Note: A continuous part of an array is a subarray.

# Input
# int[] arr: An integer array of size 
# N
# N.

# int N: The size of the array.

# Output
# Return an integer representing the total number of subarrays of size 3 such that 


# Eg1:
# Input:
# arr = [1, 2, 1, 3, 5, 2, 4, 2]
# N = 8
# Output:
# 2

def subarrray(arr):
    n = len(arr)
    cnt = 0
    for i in range(n-2):
       if arr[i] + arr[i+2] == arr[i+1]:
           cnt +=1     
    return cnt



arr = [1, 2, 1, 3, 5, 2, 4, 2]
print(subarrray(arr))
arr = [1, 3, 2, 1, 3, 2]
print(subarrray(arr))
