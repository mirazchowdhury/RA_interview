def reverse_string(s):
    reversed = ""
    for char in s:
        reversed = char + reversed
    return reversed
print(reverse_string("hello")) 
