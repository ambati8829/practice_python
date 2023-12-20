file = open("csv_data.txt", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

write_csv_path = "csv.txt"

def is_file_content_empty(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return not content.strip()

if is_file_content_empty(write_csv_path):
    write_csv = open(write_csv_path, "a")
else:
    # Open the file in write mode to clean the existing data
    write_csv = open(write_csv_path, "w")
    
for line in lines:
    data = line.split(",")
    id = data[0]
    name = data[1].title()
    department = data[2].title()
    salary = data[3]
    
    message = f"For ID number {id}, the salary is {salary} euros.\n"
    
    write_csv.write(message)

write_csv.close()
print(f"Data has been written to {write_csv_path}")
