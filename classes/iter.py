"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object
The __iter__() method acts similar as __init__(), you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows us to do operations, and must return the next item in the sequence.

"""

"""
class MyNums:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myCls = MyNums()
myIter = iter(myCls)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

"""