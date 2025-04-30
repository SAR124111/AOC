with open("day_3.txt","r") as f:
    data = f.read()

locations = {(0,0):1}

santa_x, santa_y = 0,0
robo_x, robo_y = 0,0

for i, char in enumerate(data):

    if i % 2 == 0:
        if char == '^':
            santa_y += 1
        elif char == 'v':
            santa_y -= 1
        elif char == '>':
            santa_x += 1
        elif char == '<':
            santa_x -= 1
    else:
        if char == '^':
            robo_y += 1
        elif char == 'v':
            robo_y -= 1
        elif char == '>':
            robo_x += 1
        elif char == '<':
            robo_x -= 1
    if (santa_x,santa_y) not in locations:
        locations[(santa_x,santa_y)] = 1
    if (robo_x,robo_y) not in locations:
        locations[(robo_x,robo_y)] = 1

print(len(locations))
