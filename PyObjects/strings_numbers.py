import re

# split on a delimiter into a list of substrings
line = 'aaa,bbb,cocci,dd'
print(line.split(','))  # ['aaa', 'bbb', 'cocci', 'dd']

var = '%s, eggs, and %s' % ('spam', 'SPAM!')
var2 = '{1}, eggs, and {0}'.format('spam', 'SPAM!')
print(var, '\n', var2)

# Unicode strings
print('sp\xc4m')  # 'spÄm' -> from Python 3.X, strings are Unicode-based by default
print(b'a\x01c')  # b'a\x01c' -> Bytes based data
print(u'sp\u00c4m')  # 'spÄm'

# Pattern matching
match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
print(match.group(1))


class Worker:
    def __init__(self, name, pay):  # initialize when created
        self.name = name  # self is the new object (I prefer to call it an object pointer)
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)     # Update pay in place


bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
bob.lastName()
sue.lastName()
