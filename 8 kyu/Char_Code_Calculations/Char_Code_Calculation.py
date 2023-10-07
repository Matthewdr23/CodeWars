# Given a string, turn each character into its ASCII character code and join them together to create a number - let's call this number total1:

def calc(x):
    #your code here
    arr = list(x)
    new_arr = []
    for i in x:
        ascii_convertion = ord(i)
        new_arr.append(ascii_convertion)
    list_to_String = ''.join(str(elem) for elem in new_arr)
    total_str1 = list_to_String
    total_str2 = total_str1.replace("7", "1")
    total1 = [int(x) for x in str(total_str1)]
    total2 = [int(x) for x in str(total_str2)]
    sumtotal1 = sum(total1)
    sumtotal2 = sum(total2)
    print(sumtotal1)
    print(sumtotal2)
    return sumtotal1 - sumtotal2
calc('ABC')