"""
2.4 Least Common Multiple

Task: Given two integers a and b, find their least common multiple
Input Format: The two integers a and b are given in the same line separated by a space.
Constraints: 1 <= a,b <= 2 * 10^9
Output Format: Output the least common multiple of a and b.
"""

def greatest_common_divisor(a, b):
    while b != 0:
        a_prime = b
        b = a % b
        a = a_prime
    return a

def least_common_multiple(a, b):
    gcd = greatest_common_divisor(a, b)
    lcm = (a * b) / gcd
    return lcm

def main():
    user_input = input("Enter two integers separated by a space: ")
    ints = user_input.split()
    
    a = int(ints[0])
    b = int(ints[1])
    
    result = least_common_multiple(a, b)
    print(int(result))

if __name__ == "__main__":
    main()
    
     