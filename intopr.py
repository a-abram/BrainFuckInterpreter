def parse(code):
    newCode = ''
    for c in code:
        if c in '+-><][.,':
            newCode += c
    return newCode


def block(code):
    o = []
    b = {}
    for i in range(len(code)):
        if code[i] == '[':
            o.append(i)
        elif code[i] == ']':
            b[o[-1]] = i
            b[i] = o.pop()
    return b


def run(code):
    code = parse(code)
    blocksCode = block(code)
    x = i = 0
    blocks = {0: 0}

    while i < len(code):
        symbol = code[i]
        if symbol == '>':
            x += 1
            blocks.setdefault(x, 0)
        elif symbol == '<':
            x -= 1
        elif symbol == '+':
            if blocks[x] == 255:
                blocks[x] = 0
            else:
                blocks[x] += 1
        elif symbol == '-':
            if blocks[x] == 0:
                blocks[x] = 255
            else:
                blocks[x] -= 1
        elif symbol == '.':
            print(chr(blocks[x]), end='')
        elif symbol == ',':
            blocks[x] = ord(input())
        elif symbol == '[':
            if not blocks[x]:
                i = blocksCode[i]
        elif symbol == ']':
            if blocks[x]:
                i = blocksCode[i]
        i += 1

run(input())
