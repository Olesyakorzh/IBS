"""
f = open('123.txt', 'w')
f.write('hello!')
f.close()
"""
"""
f = open('123.txt', 'r')
print(f.read())
"""
"""
f = open('123.txt', 'w')
str_list = ['Hello!\n', 'World!']
f.writelines(str_list)
f.close()
f = open('123.txt', 'r')
print(f.readline())
f.close()
f = open('123.txt', 'r')
str_list = f.readlines()
print(str_list)
"""
"""
with open('123.txt', 'w') as f:
    str_list = ['Hello!2\n', 'World!2']
    f.writelines(str_list)
    
with open('123.txt', 'r') as f:
    print(f.readline())
    
with open('123.txt', 'r') as f:
    str_list1 = f.readlines()
    print(str_list1)
    """ 
"""
for line in open('123.txt', 'r'):
    print(line)
    """ 
import os

print(os.path.exists('123.txt'))
print(os.listdir())

def show(dir):
    for name in os.listdir(dir):
        path=os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            show(path)
show('C:\\Users\\User\\Documents\\GitHub')
    
    