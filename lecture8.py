
with open('123.txt', 'r') as f:
    
    with open('321.txt', 'w') as new_f:
        
        for line in f:
            words = line.split()
            words.reverse()
            reversed_line = " ".join(words)
            new_f.write(reversed_line + "\n")
            

with open('123.txt', 'r') as f:    
    print(f.read())
with open('321.txt', 'r') as new_f:
    print(new_f.read())


    
