# 1. Maximum Permutation Value
# Problem Statement
# You are given a string array of length
# N
# N. Your task is to return the maximum permutation count of the strings after removing all the vowels ('a', 'e', 'i', 'o', 'u', both lowercase and uppercase) from every element in the string array.

# Note:

# Consider all the letters in the string as different. If the word is 'bolt' and another is 'tbol', consider both as different.

# If there are no permutable characters, return 0.

# The string consists of both uppercase and lowercase characters.

# Input
# string[] arr: A string array of length N.

# int N: Number of elements in the array.

# Output
# Return the integer value representing the maximum permutation count among all processed strings.

# Example 1
# text
# Input:
# arr = ["hello", "ccbc", "aeiou"]
# N = 3

# Output:
# 24

# Explanation:
# - "hello" → consonants "hll" (3! = 6).
# - "ccbc" → all letters (4! = 24).
# - "aeiou" → all vowels removed, 0 letters left (0 permutations).
# Maximum permutation is 24.
# Example 2
# text
# Input:
# arr = ["eio"]
# N = 1

# Output:
# 0

# Explanation:
# "eio" has only vowels; thus, no letters remain after removal. So permutations = 0.


def max_per(arr, n):
    
    vowels = set('aeiouAEIOU')
    max_consonents = 0
    
    for s in arr:
        cnt=0
        for ch in s:
            if ch not in vowels:
                cnt+=1
        max_consonents = max(max_consonents , cnt)
    
    if max_consonents == 0:
        return 0
    
    i=1
    fact = 1
    print("max: ", max_consonents)
    while i<=max_consonents:
        fact *=i
        i+=1
    
    return fact
                
#     res = []
#     # i=0
#     is_valid = False
#     for s in arr:
#         cnt = 0
#         for ch in s:
#             if ch not in "aeiouAEIOU":
#                 is_valid = True
#                 cnt += 1
#         res.append(cnt)
#     m = max(res)
#     ans = 1
#     for i in range(m, 0, -1):
        
#         ans *= i
#     # print(ans)

# # return ans if is_valid else: 0
#     if is_valid:
#         return ans
    
#     return 0
    

arr = ["hello", "ccbc", "aeiou"]
n = 3

# arr = ["eio"]
# N = 1
print(max_per(arr, n))
