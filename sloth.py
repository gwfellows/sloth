LITERAL = 0
FUNCTION = 1


def box(stack):
    print("making box with", stack[-1])
    return 1


def make_vector(stack):
    depth = int(stack[-1])
    return stack[-depth - 1 : -1]


functions = {"box": box, ",": make_vector}


def parse_literal(literal):
    if literal[0] == '"' and literal[-1] == '"':
        return literal[1:-1]
    else:
        return float(literal)


def tokenize(input):
    tokens = []
    for token in input.split():
        if token in functions:
            code, token = FUNCTION, functions[token]
        else:
            code, token = LITERAL, parse_literal(token)
        tokens.append((code, token))
    return tokens


test = """

1 2 3 3 , box

"""

def run(input):
    stack = []
    for token in tokenize(input):
        if token[0] == LITERAL:
            stack.append(token[1])
        elif token[0] == FUNCTION:
            stack.append(token[1](stack))
        print(stack)


run(test)
