# Define the sequence length & the sequence elements
array_length = int(input())
array_sequence = [int(x) for x in input().split()]

# Write the Fast Algorithm (version 1) for the Maximum Pairwise Product Problem

# Find the first largest element in the sequence
index1 = 0
for i in range(1, array_length):
    if array_sequence[i] > array_sequence[index1]:
        index1 = i

# Find the second largest element in the sequence
index2 = 0
for i in range(1, array_length):
    if array_sequence[i] != array_sequence[index1] & array_sequence[i] > array_sequence[index2]:
        index2 = i
"""
Syntax error when we test array[2, 1]
This is because the algorithm is selecting the element 2 twice.
Need to refactor the code to remove the first selected (largest) element before the second scan.
"""
        
# Calculate the product of the element at Index1 and Index2
print(array_sequence[index1] * array_sequence[index2])
    




