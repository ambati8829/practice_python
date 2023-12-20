friends= input("Enter three names with a space between: ").split()

people = open("people.txt","r")
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby = friends_set.intersection(people_nearby_set)

nearby_friends_file = open("nearby_friends.txt", "w")

for i in friends_nearby:
    nearby_friends_file.write(f"{i}\n")

nearby_friends_file.close()
