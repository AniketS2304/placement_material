# Problem Statement
# You need to arrange books in a library with the help of students. Each student has a collection of books. Bookshelves can hold a maximum of 
# K
# K books and must be fully loaded. If a student has more than shelf capacity, excess books carry over to the next student's shelf. If they have fewer books, those books carry over to the next shelf. If the last student has any extra/fewer books, those books are discarded.
# Your task is to return the total number of fully decked bookshelves.

# Input
# int N: Number of students.

# int K: Maximum number of books a shelf can hold.

# int[] arr: Array representing the number of books each student has.

# Output
# Return the integer value representing the total number of bookshelves that are completely decked by the books.


def full_shelves(n,k,arr):
    curr = 0
    full_shelves = 0
    
    for book in arr:
        curr += book
        
        while curr >= k:
            full_shelves +=1
            curr -= k
    
    return full_shelves



N = 5
K = 10
arr = [12, 5, 7, 15, 3]  # example input
print(full_shelves(N, K, arr))