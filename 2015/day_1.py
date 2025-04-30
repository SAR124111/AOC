with open('day_1.txt','r') as file:
    content = file.read()
score = 0
index = 0
for character in content:
   
    if character == '(':
        score += 1
        index += 1
    elif character == ')':
        score -= 1
        index += 1
        if score == -1:
            print(index)
            break   

     
print(score)





