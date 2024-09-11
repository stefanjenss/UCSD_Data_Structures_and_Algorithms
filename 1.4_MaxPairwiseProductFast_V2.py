# Define the sequence length & the sequence elements
array_length = int(input())
array_sequence = [int(x) for x in input().split()]

# Write the Fast Algorithm (version 1) for the Maximum Pairwise Product Problem

# Find the first largest element in the sequence
index1 = 0
for i in range(1, array_length):
    if array_sequence[i] > array_sequence[index1]:
        index1 = i

# Check whether index1 == 0. If so, make index2 = 1
# {Ensures that index2 will not equal index1}
if index1 == 0:
    index2 = 1
else:
    index2 = 0

# Find the second largest element in the sequence
for i in range(1, array_length):
    if array_sequence[i] != array_sequence[index1] & array_sequence[i] > array_sequence[index2]:
        index2 = i

        
# Calculate the product of the element at Index1 and Index2
print(array_sequence[index1] * array_sequence[index2])

"""
Another Syntax Error!
Time to Stress Test!
This program ultimately fails because it is unable to account for situations in which the two largest elments
in the sequence are the same number (i.e., 9 1 1 2 9 | which outputs 9 instead of 81)
"""




