class FirstHundredGenerator:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<5:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

for i in FirstHundredIterable():
    print(i)
    
#The above for loop prints the answer like 0/n1/n2/n3/n4/n5. Instead of calling  a separate class for iterable, we can include __iter__ in the FirstHundredGenerator class itself o do the iteration.

class FirstHundredGenerator:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<5:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self

for i in FirstHundredGenerator():
    print(i)

# This generator is both iterator and iterable.

class AnotherIterator:
    def __init__(self):
        self.cars = ['Tata','Mahindra']
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,i):
        return self.cars[i]
    
for car in AnotherIterator():
    print(car)

#Here AnotherIterator is an iterable even though it doesn't contain an iterable method in it. In python we can define the iterable methods by either __iter__ method or by and object that contains both "__len__ and __getitem__" methods.
#Iterator: used to get the next value.
#Iterable: used to go over all the values of the iterator.


my_numbers = [x for x in [1,2,3,4]] #This is list comprehension, which copies entire list and gives that.
my_numbers_gen = (x for x in [1,2,3,4,5]) #This is not a tuple comprehension, This is a generator comprehension. This will go over list and yield each number as we call next. This will go through one by one with out copying the entire list.

print(next(my_numbers_gen))