class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, objtype=None):
        if self.fget is None:
            raise AttributeError()
        return self.fget(obj)

    def __set__(self, obj, val):
        if self.fset is None:
            raise AttributeError()
        self.fset(obj, val)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError()
        self.fdel(obj)

    def setter(self, fset):
        return Property(self.fget, fset, self.fdel)

    def getter(self, fget):
        return Property(fget, self.fset, self.fdel)
