def even_numbers_up_to_n(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            pass  
    return evens
print(even_numbers_up_to_n(10))  
