from property import Property

class Human(object):
    def __init__(self):
        self._age = 0

    def _get_age(self):
        return self._age

    def _set_age(self, val):
        if val < 0:
            raise TypeError()
        else:
            self._age = val

    def _del_age(self):
        del self._age

    age = Property(_get_age, _set_age, _del_age)

class Human2(object):
    def __init__(self):
        self._age = 0

    age = Property()

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val < 0:
            raise TypeError('Age should be positive')
        else:
            self._age = val

    # @Property.deleter
    # def age(self):
    #     del self._age

    # age = Property(_get_age, _set_age, _del_age)

me = Human2()
print(me.age)
me.age = 19
print(me.age)
