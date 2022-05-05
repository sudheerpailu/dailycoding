'''There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.'''

def unique_ways(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

n=int(input())
print(unique_ways(n))