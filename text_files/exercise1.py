open_file = open("questions.txt","r")
Q_A_list = [line.strip() for line in open_file.readlines()]

open_file.close()

score = 0
total = len(Q_A_list)

for i in Q_A_list:
    q, a = i.split("=")
    ans = input(f"{q}=")
    
    if a==ans:
        score+=1

result= open("result.txt","w")
result.write(f"Your final score is {score}/{total}.")
result.close()