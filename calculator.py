
def parse(s):
    x,s = parse_a(s)
    assert(len(s) == 0)
    return x

def parse_a(s):
    if s[0] == '(':
        x, s = parse_a(s[1:])
        if s[0] == '+':
            y, s = parse_a(s[1:])
            assert(s[0] == ')')
            return x+y, s[1:]
        elif s[0] == '*':
            y, s = parse_a(s[1:])
            assert(s[0] == ')')
            return x*y, s[1:]
    else:
        assert(int(s[0]) > -1 and int(s[0]) < 10)
        return int(s[0]), s[1:]


def add(s):
    i = s.index('+')
    a = s[:i]
    b = s[i+1:]
    arg1 = int(a.strip())
    arg2 = int(b.strip())
    return arg1 + arg2

def assertEquals(x, s):
    y = parse(s)
    if x != y:
        print("Error: expected " + str(x) + " but got " + str(y))

if __name__ == "__main__":
    assertEquals(1 + 2, '(1+2)')
    assertEquals(1 * 2, '(1*2)')
    assertEquals(1 + (2 * 3), '(1+(2*3))')
    assertEquals(0 + (2 * 3), '(1+(2*3))')
