directions = open('inputs/day3', 'r').read()

grid = {(0, 0)}

def calculate(directions):
    x = 0
    y = 0
    for dir in directions:
        if dir == '^':
            x += 1
        elif dir == 'v':
            x -= 1
        elif dir == '>':
            y += 1
        elif dir == '<':
            y -= 1
        grid.add((x, y))

calculate(directions[::2])
calculate(directions[1::2])

print "Solution #2: \n" + str(len(grid))