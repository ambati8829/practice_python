
# filter function
cars = ['Tata','Mahindra','Ferrari', 'Mercedes', 'Ford', 'Toyota']

start_with_t = filter(lambda x: x.startswith('R'), cars) # This produces a generator meaning that it yield one value for each next.

print(next(start_with_t))
print(next(start_with_t))

another_starts_with_t= (f for f in cars if f.startswith('T')) #This is similar to start_with_t. Gives same answer. This way is called as generator comprehension.

print(next(another_starts_with_t))
print(next(another_starts_with_t))

#map() function
cars_lower = map(lambda x: x.lower(), cars)

print(next(cars_lower))

another_cars_lower = (f.lower() for f in cars) #similar to cars_lower.

print(next(another_cars_lower))

#any() function
friends = [
    {
        'name': 'Ambati',
        'location': 'Guntur'
    },
    {
        'name': 'Sandeep',
        'location': 'Macherla'
    },
    {
        'name': 'Sunny',
        'location': 'Guntur'
    }
]

your_location = input("Where is your location: ")

friends_nearby = [friend for friend in friends if friend['location']==your_location]

if any(friends_nearby):
    print(f"You can go out with {friends_nearby}")
    
#all() function 
print(all([1,2,3,4]))
print(all([0,1,2,3,4]))
