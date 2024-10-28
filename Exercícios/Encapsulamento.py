class Foo:
    def __init__(self):
        self.public = 'Public'
        self.__private = 'Private'
        self._protected = 'Protected'

    def __private(self):
        return 'Private'
    
    def _protected(self):
        return 'Protected'

foo = Foo()
print(foo.public)

