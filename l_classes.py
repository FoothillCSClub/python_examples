class Foo:

    def __init__(self):
        print('created Foo')
        self.a = 5

    def print_a(self):
        print(self.a)


foo = Foo()
foo.print_a()

foo.a = 2
foo.print_a()
