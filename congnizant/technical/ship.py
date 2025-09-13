# 2. Ship Rounds
# Problem Statement
# A ship needs to transport a certain number of people from Point A to Point B. The capacity of the ship is denoted by integer C, and the total number of people to be transported is denoted by integer N.
# Your task is to return the minimum number of rounds the ship needs to make to transport all people from Point A to Point B.
# Note: One round consists of the ship traveling from Point A to Point B and then returning to Point A.

# Input
# int C: Capacity of the ship.

# int N: Total number of people to be transported.

# Output
# Return an integer representing the number of rounds needed.

# Example 1
# text
# Input: 
# C = 4
# N = 10
# Output: 
# 3

# print

def min_rounds(c,n):
    return (n+c-1)//c

print(min_rounds(4,10))
print(min_rounds(4,8))
print(min_rounds(4,2))
print(min_rounds(4,15))