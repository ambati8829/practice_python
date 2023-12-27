#range function

#def hundred_numbers():
#   nums = []
#   i = 0
#   while i<100:
#       nums.append(i)
#       i+=1
#  return nums

#print(hundred_numbers())

#The above function is similar to below function which is called as Generator function

def hundred_numbers():
    i=0
    while i<100:
        yield i
        i+=1

#print(hundred_numbers())
#This will print "<generator object hundred_numbers at 0x0000029BE93B5D80>". This is generator object because it uses yield. yield is where the generator function1(iteration) stops until what we asked for.

g = hundred_numbers()
#print(next(g))
# Generator is stored in a variable. We can call this variable how many times we want without calling all the 100 values in that list. This above print statement will give us "0".

#print(next(g))
#print(next(g))
#This will print 0/n1

print(next(g))
print(next(g))
print(list(g))

#This will print 0/n1/n[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
#60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]