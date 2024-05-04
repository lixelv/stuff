class MyNumber(int):
    def __new__(cls, *key, **kwkey):
        return super(MyNumber, cls).__new__(cls, *key, **kwkey)

a = MyNumber(5)
a.d = 6

print(a, a.d)
