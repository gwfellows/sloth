LITERAL = 0
FUNCTION = 1


def box(stack):
    print("making box with", stack[-1])
    return stack


functions = {"box": box}


def parse_literal(literal):
    if literal[0] == '"' and literal[-1] == '"':
        return literal[1:-1]
    else:
        return float(literal)


def tokenize(s):
    tokens = s.replace("[", " [ ").replace("]", " ] ").split()

    def parse_tokens(tokens):
        result = []
        while tokens:
            token = tokens.pop(0)
            if token == "[":
                result.append(parse_tokens(tokens))
            elif token == "]":
                return result
            else:
                try:
                    result.append(
                        (FUNCTION, functions[token])
                        if token in functions
                        else (LITERAL, parse_literal(token))
                    )  # int(token))
                except ValueError:
                    result.append(token)
        return result

    return parse_tokens(tokens)


test = '[1] [2] [[3] [4 [4 4 4]]] [1.5 [ 6 1 4] "blue"] box'

# print(tokenize(test))
# exit()


def run(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, list):
            stack.append(run(token))
        elif token[0] == LITERAL:
            stack.append(token[1])
        elif token[0] == FUNCTION:
            stack = token[1](stack)
        print(stack)
    return stack


print(tokenize(test))
run(tokenize(test))
