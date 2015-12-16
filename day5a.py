def check_vowels(string):
    list = ['a', 'e', 'i', 'o', 'u']
    vowels = 0

    for char in list:
        vowels += string.count(char)

    if vowels >= 3:
        return True
    return False


def check_duplicates(string):
    checked = ''

    for char in string:
        if char == checked:
            return True
        checked = char
    return False


def check_disallowed(string):
    disallowed = 0
    disallowed += string.count('ab')
    disallowed += string.count('cd')
    disallowed += string.count('pq')
    disallowed += string.count('xy')

    if disallowed == 0:
        return True
    return False

def main():
    file = open('inputs/day5', 'r')

    counter = 0

    for l in file:
        if check_vowels(l) & check_duplicates(l) & check_disallowed(l):
            counter += 1

    print counter


if __name__ == '__main__':
    main()
