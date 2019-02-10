presents = open('input2.txt', 'r')
box_list = []
for present in presents:
    line = present.strip()
    box_list.append(line.split('x'))
print(box_list)

paper_sum = 0
box_num = 1
for box in box_list:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    min_side = min(l*w, w*h, h*l)
    print('box ', box_num, ': \nlength: ', l,
          '\nwidth: ', w, '\nheight: ', h)
    print('min_side = ', min_side)

    surface_area = 2*l*w + 2*w*h + 2*h*l + min_side
    print('surface_area = ', surface_area)
    paper_sum += surface_area
    print('===========')
    box_num += 1

print(paper_sum)
