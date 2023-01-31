#! main
# This is a means of running Bash scripts with Python commands/statements.
# Imports are too expensive, modules should only be imported once, otherwise,
# reload() function is used.

import sys
print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)
print('The Bright Side' + 'of Life...')
print(list(range(10)))
import random
print(random.random())
print(random.choice([1,2,3,4,5,6]))
# input('Press Enter to Exit')

# bytearray type for joining and extending characters
B = bytearray(b'spam')
B.extend(b'eggs')
print(B.decode())