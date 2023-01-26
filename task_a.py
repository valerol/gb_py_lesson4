from random import randint
def generatePolynom(k):
    polynom = ''
    for i in range(k, -1, -1):
        polynom += f"{randint(-100, 100)}*pow(x,{i})"
        if i > 0:
            polynom += ' + '
        else:
            polynom += ' = 0 '
    return polynom

f = open("polynom1.txt", "w")
f.write(generatePolynom(randint(1, 10)))
f.close()

f = open("polynom2.txt", "w")
f.write(generatePolynom(randint(1, 10)))
f.close()
