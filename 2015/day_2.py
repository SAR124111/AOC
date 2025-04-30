with open("day_2.txt","r") as file:
    dimensions = [list(map(int, line.strip().split('x'))) for line in file]
final_amount = 0
ribbon_total_length = 0
for h,w,l in dimensions:
    area = 2*h*w + 2*h*l + 2*w*l
    ribbon = min(h+w, h+l, w+l) * 2
    ribon_extra = h*w*l
    ribbon_total_length += ribbon + ribon_extra
    slack = min(h*w, h*l, w*l)
    total_area = area + slack
    final_amount += total_area

print(final_amount)
print(ribbon_total_length)