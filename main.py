#!/usr/bin/python3


from stack import Stack
from parser import parse
import shared, util


def exec(stack, toks):
    for tok_type, tok_value in toks:
        if tok_type == 'number':
            stack.push(tok_value)
            continue

        shared.OPERATORS[tok_value](stack)


if __name__ == '__main__':
    stack = Stack()
    util.log('Stack initialized. Listening...')
    while True:
        exec(  stack, parse( input('> ') )  )
