#Ray Tso
#3/1/18
#warmup9.py

word = input('Enter a word: ')
for ch in word:
    if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
        print(ch.upper())
    else:
        print(ch)
