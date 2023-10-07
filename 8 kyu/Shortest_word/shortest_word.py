# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    # your code here
    print(min(len(x) for x in s.split()))

    # return l # l: shortest word length

find_short("bitcoin take over the world maybe who knows perhaps")