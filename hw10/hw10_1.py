with open('file.txt','r') as f:
    file = f.read()

def longest_words():
    s = file.split()
    print(max(s, key=len))

longest_words()


