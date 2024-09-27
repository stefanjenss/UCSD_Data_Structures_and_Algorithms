"""
Task: Given an integer n, find the nth Fibonacci number F(n).
Input Format: The input consists of a single integer n.
Constraints: 0 <= n <= 45
Output Format: Output F(n)
"""

def fibonacci(n):
    # If n <= 1, we simply return n
    if n <= 1:
        return(n)
    
    else:
        prev, current = 0, 1
        for _ in range(2, n + 1):
            prev, current = current, prev + current
        return (current)

def main():
    n = int(input())
    result = fibonacci(n)
    print(result)
    
if __name__ == "__main__":
    main()