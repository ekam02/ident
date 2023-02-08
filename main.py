from random import Random


letter = Random()
alpabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
print(''.join(letter.choices(alpabet, k=8)))