import shared, util


def parse(line):
    return tokenize( line.split() )


def tokenize(items):
    toks = []

    for it in items:
        if it in shared.OPERATORS:
            toks.append( ('operator', it) )
            continue

        number_type = float if '.' in it else int
        try:
            toks.append(  ( 'number', number_type(it) )  )
        except ValueError:
            util.err(f'Invalid item \'{it}\' in stream.')

    return toks
