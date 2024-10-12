LITERAL = 0
FUNCTION = 1


def tokenize(input):
    return input.split()

test = """

10x10x10 box
"""

def run(input):
    stack = []
    for token in tokenize(input):
        if token[0] == LITERAL:
            stack.push(token[1])
        elif token[0] == FUNCTION:
            stack = token[1](stack)


run(test)