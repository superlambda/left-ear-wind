def coro():
    x = yield
    print(x)

g = coro()
next(g)
g.send(10)  # 输出 10