class MyNumber(int):
    def __new__(cls, *args, **kwargs):
        return super(MyNumber, cls).__new__(cls, *args, **kwargs)

a = MyNumber(5)
a.d = 6

print(a, a.d)
