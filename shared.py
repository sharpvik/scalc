import sys, util


def unary(func):
    def foo(stack):
        if len(stack) < 1:
            util.log(f'Stack is too small for {func.__name__}. Skipping...')
            return
        func(stack)

    return foo

def binary(func):
    def foo(stack):
        if len(stack) < 2:
            util.log(f'Stack is too small for {func.__name__}. Skipping...')
            return
        func(stack)

    return foo


@binary
def add(stack):
    stack.push( stack.pop() + stack.pop() )

@binary
def sub(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x - y)

@binary
def mul(stack):
    stack.push( stack.pop() * stack.pop() )

@binary
def div(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x / y)

@binary
def pwr(stack):
    y, x = stack.pop(), stack.pop()
    stack.push(x ** y)

@unary
def fac(stack):
    x = abs(  int( stack.pop() )  )
    f = 1
    for i in range(1, x + 1):
        f *= i
    stack.push(f)

@unary
def eql(stack):
    print( stack.peek() )

@unary
def pop(stack):
    stack.pop()

@unary
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
