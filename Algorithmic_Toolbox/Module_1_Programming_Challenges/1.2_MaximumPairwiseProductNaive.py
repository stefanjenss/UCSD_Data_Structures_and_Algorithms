"""
This Python script finds the maximum pairwise product of two distinct numbers in a sequence
of non-negative integers
"""

n = int(input())

a = [int(x) for x in input().split()]

product = 0

for i in range(n):
    for j in range(i+1, n):
        product = max(product, a[i] * a[j])

print(product)

"""
This code will result in a "Time Limit Exceeded" error message.
So, we will need to revise the code to take less time to run.
"""