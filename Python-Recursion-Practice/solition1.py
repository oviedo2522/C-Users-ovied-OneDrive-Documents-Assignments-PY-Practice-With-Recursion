# Write code for algorithm 1 below

def count_down(n):

    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    else:
        print(n)
        return count_down(n-1)
    
    # Test the function
    n=8