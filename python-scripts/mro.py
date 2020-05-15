import io
import numbers
import tkinter


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


# class D(B, C):
class D(C, B):
    def ping(self):
        super().ping()
        # A.ping(self)
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


print(D.__mro__)
d = D()
print(hex(id(d)))
d.pong()
C.pong(d)
d.ping()
print("#####")
d.pingpong()

print(bool.__mro__)


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(bool)
print_mro(numbers.Number)
print_mro(io.BytesIO)
print_mro(tkinter.Text)
