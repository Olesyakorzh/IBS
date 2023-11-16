lst = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def odd_numbers(num):
    if(num%2 != 0) and num > 50:
        return True
    else:
        return False
    
print(list(filter(odd_numbers, lst)))

    
