class myClass:
    """A simple example class"""
    i =12345

    def f(self):
        return 'Hello world!'


mCl = myClass()
print(mCl.__doc__)
aux = mCl.f()
print(aux)