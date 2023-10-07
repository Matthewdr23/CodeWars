# Build a function that returns an array of integers from n to 1 where n>0.
def reverse_seq(n):
    if n <= 0:
        return []
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result