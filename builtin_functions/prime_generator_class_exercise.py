
class PrimeGenerator:
    def __init__(self,stop):
        self.stop = stop
        self.number=2
    def __next__(self):
        for n in range(self.number,self.stop):
            for x in range(2,n):
                if n%x ==0:
                    break
            else:
                self.number = n+1 
                return n 
        
        raise StopIteration()
    
prime=PrimeGenerator(10)

print(next(prime))

print(next(prime))

print(next(prime))

print(next(prime))

print(next(prime))
