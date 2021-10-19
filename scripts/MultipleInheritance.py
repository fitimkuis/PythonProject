class A(object):
    def __init__(self, a, *args, **kwargs):
        print("A", a)

class B(A):
    def __init__(self, b, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)
        print("B", b)

class A1(A):
    def __init__(self, a1, *args, **kwargs):
        super(A1, self).__init__(*args, **kwargs)
        print("A1", a1)

class B1(A1, B):
    def __init__(self, b1, *args, **kwargs):
        super(B1, self).__init__(*args, **kwargs)
        print("B1", b1)


B1(a1=6, b1=5, b="hello", a=None)