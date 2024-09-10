"""
In this script, we will write a Python script that sums two digits (0 <= x <= 9) that are given
as a string separated by a space.
"""
import sys

# Get the input
input_str = input("Enter two numbers separated by space: ")

# Split the input into two tokens
tokens = input_str.split()

# Define a and b from the tokens (save as integer)
a = int(tokens[0])
b = int(tokens[1])

# Sum the tokens together (print the sum)
print(a + b)