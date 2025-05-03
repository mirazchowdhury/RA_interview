def sum_of_even_numbers(n):
    i = 2
    sum = 0
    while i<=n:
        sum += i
        i += 2
    return sum
print(sum_of_even_numbers(6))  