directions = open('inputs/day3', 'r').read()

grid = {(0, 0)}

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

print "Solution #1: \n" + str(len(grid))
