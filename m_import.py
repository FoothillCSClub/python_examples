# import a whole module
import l_classes


a = l_classes.Foo()
a.print_a()


# import a specific value

from l_classes import Foo

b = Foo()
b.print_a()
