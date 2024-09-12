# Define the sequence length & the sequence elements
array_length = int(input())
array_sequence = [int(x) for x in input().split()]

# Write the Fast Algorithm (version 1) for the Maximum Pairwise Product Problem

# Find the first largest element in the sequence
index1 = 0
for i in range(1, array_length):
    if array_sequence[i] > array_sequence[index1]:
        index1 = i

# Check whether the first largest element is at index = 0, if so, start index2 at 1
if index1 == 0:
    index2 = 1
else:
    index2 = 0
        
# Find the second largest element in the sequence
for i in range(array_length):
    if i != index1 and array_sequence[i] > array_sequence[index2]:
        index2 = i

        
# Calculate the product of the element at Index1 and Index2
print(array_sequence[index1] * array_sequence[index2])




