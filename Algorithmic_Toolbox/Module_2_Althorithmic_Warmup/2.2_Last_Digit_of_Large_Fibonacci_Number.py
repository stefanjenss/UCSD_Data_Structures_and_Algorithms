"""
Last Digit of a Large Fibonacci Number

Problem Description:
-   Task: Given an integer n, find the last digit of the nth Fibonacci
    number F(n) (that is, F(n) mod 10).
-   Input Format: The input consists of a single integer n.
-   Constraints: 0 <= n <= 10^7.
-   Output Format: Output the last digit of F(n).
"""

def get_last_fibonacci_digit(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current, (previous + current) % 10
    return current

def main():
    n = int(input())
    result = get_last_fibonacci_digit(n)
    print(result)

if __name__ == "__main__":
    main()