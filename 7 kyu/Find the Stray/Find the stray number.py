# DESCRIPTION:
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

def Stray(arr):
    print(arr.sorted())
    a = arr[0]
    b = arr[1]
    c = arr[-1]
    if(a == b):
        return c
    else:
        return a
    pass