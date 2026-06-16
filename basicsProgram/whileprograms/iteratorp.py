"""
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
iterator an iterator is an aobject thet returns elemnt one by one using the next()
__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.
"""
l=[1,2,3,4]
lt=iter(l)
print(next(lt))
print(next(lt))
print(next(lt))
print(next(lt))

#print(next(lt))#throw exception StopIteration