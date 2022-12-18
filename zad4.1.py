mport
random
poliOrder = int(input("Введите максимальную степень"))
poliCoef = {}
for i in range(poliOrder + 1):
    poliCoef[i] = random.randint(-100, 100)
print(poliCoef)

polinom = ''
for i in range(poliOrder, -1, -1):
    if poliCoef[i] > 0:
        if poliCoef[i] == 1:
            if i == 1:
                polinom += f' +x'
            elif i == 0:
                polinom += f' +1'
            else:
                polinom += f' +x**{i}'
        else:
            if i == 1:
                polinom += f' +{poliCoef[i]}*x'
            elif i == 0:
                polinom += f' +{poliCoef[i]}'
            else:
                polinom += f' +{poliCoef[i]}*x**{i}'

    elif poliCoef[i] < 0:
        if poliCoef[i] == -1:
            if i == -1:
                polinom += f' -x'
            elif i == 0:
                polinom += f' -1'
            else:
                polinom += f' -x**{i}'
        else:
            if i == 1:
                polinom += f' {poliCoef[i]}*x'
            elif i == 0:
                polinom += f' {poliCoef[i]}'
            else:
                polinom += f' {poliCoef[i]}*x**{i}'

polinom.strip()
if polinom[1] == "+":
    polinom = polinom.replace("+", "", 1)
print(polinom + '= 0')
with open('output.txt', 'w') as data:
    data.write(polinom)
