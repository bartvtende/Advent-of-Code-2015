def check_double_pairs(string):
    for i in range(0, len(string) - 1):
        substring = string[i:i + 2]
        if string.count(substring) >= 2:
            return True
    return False


def check_repeats(string):
    for i in range(0, len(string)):
        if i >= 2:
            if string[i] == string[i - 2]:
                return True
    return False


def main():
    file = open('inputs/day5', 'r')

    counter = 0

    for l in file:
        if check_double_pairs(l) & check_repeats(l):
            counter += 1
            print l

    print counter


if __name__ == '__main__':
    main()
