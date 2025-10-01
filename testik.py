x=1
def foo():
    globals()["x"] = 2
    def bar():
        print(x)
    bar()
foo()

result = 20/2+12*2-9
print(result)