squaremeters = 0
meters = 0
with open('inputs/day2', 'r') as file:
    for line in file:
        splitted_line = line.split('x')
        splitted_line[2] = splitted_line[2].rstrip()  # Remove the newline
        splitted_line = map(int, splitted_line)  # Cast to an integer

        calcs = {'lw': 2 * splitted_line[0] * splitted_line[1],
                 'wh': 2 * splitted_line[1] * splitted_line[2],
                 'hl': 2 * splitted_line[2] * splitted_line[0]}

        sorted_line = sorted(splitted_line)
        min_value = min(calcs.values())
        squaremeters += (calcs['lw'] + calcs['wh'] + calcs['hl'] + (min_value / 2))
        meters += (sorted_line[0] * 2 + sorted_line[1] * 2) + (sorted_line[0] * sorted_line[1] * sorted_line[2])

print "Solution #1: \n" + str(squaremeters) + "\n"
print "Solution #2: \n" + str(meters)