# Instead of getters + setters, python uses @properties


class SomeClass:
    def __init__(self):
        self.a = 5


instance_a = SomeClass()
instance_a.a = 6
print(f'a value: {instance_a.a}')


class SomeClassImproved:
    def __init__(self):
        self._a = 5

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, new_value):
        print(f'new value set: {new_value}')
        self._a = new_value


instance_b = SomeClassImproved()
print(f'b starting value: {instance_b.a}')

instance_b.a = 27
print(f'b new value: {instance_b.a}')
