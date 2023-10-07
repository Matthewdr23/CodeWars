#Instructions
# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    # Your code here
    pos_only = []
    neg_Only = []
    for element in arr :
        if element > 0:
            pos_only.append(element)
        else:
            neg_Only.append(element)
    return sum(pos_only)
    if arr == []:
        return 0
    
positive_sum([1,-4,7,12])

# this is the most O(n) answer
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#Link to other solutions
#https://www.codewars.com/kata/5715eaedb436cf5606000381/solutions/python