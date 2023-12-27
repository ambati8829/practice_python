class FirstHundredGenerator:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<100:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
    
my_gen = FirstHundredGenerator()

print(next(my_gen))
print(next(my_gen))
#This wil print out 0/n1. The class is a new way of defining a generator, which refer to as generator class or class-based generator.