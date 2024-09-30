"""
2.3 Greatest Common Divisor

Task: Given two integers a and b, find their greatest common divisor.
Input Format: The two integers a, b are given in the same line separated by a space.
Constraints: 1 <= a, b <= 2 * 10^9
Output Format: Output(a,b)
"""

def euclidGCD(a, b):
    if b == 0:
        return a
    aPrime = a % b
    return euclidGCD(b, aPrime)

def main():
    input_str = input("Input two integers separated by a space:")
    ints  = input_str.split()
    a = int(ints[0])
    b = int(ints[1])
    result = euclidGCD(a, b)
    print(result)
    
if __name__ == "__main__":
    main()