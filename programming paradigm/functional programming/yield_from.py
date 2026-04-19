def sub():
    yield 1
    yield 2

def main():
    yield from sub()