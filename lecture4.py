dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dct = {}
for key, value in dct.items():
    if value >= 3:
        new_dct[key] = value
     
print(new_dct)