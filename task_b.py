import itertools
def parcePolynom(filename):
    f = open(filename, "r")
    polynom = f.read()
    f.close()

    print(polynom)
    polynom = polynom.replace(' ', '').replace('=0', '').split('+')

    polynom.reverse()

    for i, member in enumerate(polynom):
        polynom[i] = int(member.split('*')[0])

    return polynom

poliNums1 = parcePolynom("polynom1.txt")
poliNums2 = parcePolynom("polynom2.txt")

poliSums = [int(x or 0) + int(y or 0) for x, y in itertools.zip_longest(poliNums1, poliNums2)]

for i in range(0, len(poliSums)):
    poliSums[i] = f"{poliSums[i]}*pow(x, {i})"

poliSums.reverse()

polySum = ' + '.join(poliSums) + ' = 0'

print(polySum);
f = open("polysum.txt", "w")
f.write(polySum)
f.close()



