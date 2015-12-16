import hashlib

input = "ckczppom"

inc = 0

def calculate(zeroes):
    inc = 0
    while True:
        inc += 1
        m = hashlib.md5()
        m.update(input + str(inc))
        m.digest()
        if m.hexdigest().startswith(zeroes):
            return input + str(inc)

print "Solution #1:\n" + calculate("00000")
print "\nSolution #2:\n" + calculate("000000")