def move(directions):
    floor = 0
    position = 0
    with open(directions) as file:
        for line in file:
            for instruction in line:
                if instruction == "(":
                    floor = floor + 1
                elif instruction == ")":
                    floor = floor - 1

                position += 1
                if floor < 0:
                    print(position)
    print(floor)


move("C:\\scripts\\advent\\input.txt")
