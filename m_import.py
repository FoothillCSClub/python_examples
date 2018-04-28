# import a whole module
import j_classes


a = j_classes.Foo()
a.print_a()


# import a specific value

from j_classes import Foo

b = Foo()
b.print_a()
