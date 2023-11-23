import sys

word = sys.stdin.readline().rstrip()
filename = sys.stdin.readline().rstrip()

with open(filename, 'rb') as ff:
    while True:
        current = ff.readline()
        if not current:
            break
        if word.encode('utf-8') in current:
            print(f"find: {filename} {word}")
            