import random

# Define the maxPairwiseProductNaive function
def maxPairwiseProductNaive(n, array):
    # Initialize the maxProd to 0
    maxProd = 0
    """
    Iterate through the array, multiplying each element by every element that follows
    and comparing that to the previous max product.
    """
    for i in range(n):
        for j in range(i+1, n):
            maxProd = max(maxProd, array[i] * array[j])
    return maxProd

# Define the maxPairwiseProductFast (w/ potential bug) function
def maxPairwiseProductFast(n, array):
    # Find the first largest element in the array sequence
    # Initialize the index to 0
    index1 = 0
    for i in range(1, n):
        if array[i] > array[index1]:
            index1 = i
            
    # Check whether the first largest element is at index = 0, if so, start index2 at 1
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
        
    # Find the second larhest element in the array sequence
    for i in range(n):
        if i != index1 and array[i] > array[index2]:
            index2 = i
    # Calculate the product of the two largest elements in the array
    print(index1, index2)
    return(array[index1] * array[index2])

# Define the stressTest function
def stressTest(N, M):
    while True:
        # Generate a random integer for n (the number of elements in the array)
        n = random.randint(2, N)
        # Generate an array of random integers between 0 and M of length n
        array = [random.randint(0, M) for _ in range(n)]
        
        # Display the random array generated for the test case
        print(array)
        
        # Run the test case using the two functions to generate `result1` and `result2`
        result1 = maxPairwiseProductNaive(n, array)
        result2 = maxPairwiseProductFast(n, array)
        
        # Evaluate whether the results are the same (test passed) or if they differ (test failed)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer", result1, result2)
            return
        
# Run the stress test
stressTest(5, 10)