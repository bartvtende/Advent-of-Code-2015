file = open('inputs/day1', 'r')

sentence = file.readline()

first = 0
second = 0
solution2 = 0

for i in range(0, len(sentence)):
    if sentence[i] == '(':
        first += 1
    elif sentence[i] == ')':
        second += 1
    if first == second & solution2 == 0:
        solution2 = i + 2

print "Solution #1: \n" + str(first - second) + "\n"
print "Solution #2: \n" + str(solution2)
