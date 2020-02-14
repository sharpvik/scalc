#!/usr/bin/python3


from stack import Stack
from parser import parse
from shared import OPERATORS


def exec(stack, toks):
    for tok_type, tok_value in toks:
        if tok_type == 'number':
            stack.push(tok_value)
        else:
            OPERATORS[tok_value](stack)


if __name__ == '__main__':
    stack = Stack()
    while True:
        exec(  stack, parse( input('> ') )  )
