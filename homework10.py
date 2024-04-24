def test():
    a = 4
    b = 6
    print(a, b)
    print()

def test2(a = 7, b = 4, c = 8):
    print(a, b, c)

test()

test2()
test2(1)
test2(c=6)
test2(3, 5, 9)
