
dct = {'key':'val'}
print(dct.keys())
###
dct = {}
dct['key'] = 'val'
print(dct)
###
dct = dict(kkl='val')
print(dct)
###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
print(dct)
###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
print('key1' in dct)
###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
print({}.fromkeys(['key3', 'key4'], 111))
###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
print(dct.get('key3'))
###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
for k, v in dct.items():
    print(v)
    ###
    dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
    print(dct.values())
    ###
dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
for k in dct:
    print(k)
    ###
def hist(s):
    d=dict()
    for c in s:
        if c not in d: d[c]=1
        else: d[c]+=1
    return d

print(hist('how many times'))
### выводим ключи
dct = {'key2': 'val1', 'key1': 'val2'}
ls = list(dct.keys())
ls.sort()
for k in ls:
    print(k)
### выводим значения
dct = {'key2': 'val1', 'key1': 'val2'}
ls = list(dct.keys())
ls.sort()
for k in ls:
    print(dct[k])
### задание
dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dct = {}
for key, value in dct.items():
    if value >= 3:
        new_dct[key] = value
     
print(new_dct)
        
    