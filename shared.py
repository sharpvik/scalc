import sys


def add(stack):
    stack.push( stack.pop() + stack.pop() )

def sub(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x - y)

def mul(stack):
    stack.push( stack.pop() * stack.pop() )

def div(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x / y)

def pwr(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x ** y)

def fac(stack):
    x = int( stack.pop() )
    f = 1
    for i in range(1, x + 1):
        f *= i
    stack.push(f)

def eql(stack):
    print( stack.peek() )

def pop(stack):
    stack.pop()

def emt(stack):
    print( stack.pop() )

def dis(stack):
    print(stack)

def ext(stack):
    sys.exit(0)


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '^': pwr,
    '!': fac,
    '=': eql,
    '#': pop,
    '$': emt,
    '?': dis,
    'q': ext,
}
