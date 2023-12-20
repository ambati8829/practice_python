import json

json_list=[]
csv_file= open("test_csv_file.txt")

for line in csv_file.readlines():
    club, city, country = line.strip().split(",")
    data= {
        'club': club,
        'city': city,
        'country': country
    }
    
    json_list.append(data)

csv_file.close()

json_file=open("test_json.txt","w")
json.dump(json_list, json_file)

json_file.close()