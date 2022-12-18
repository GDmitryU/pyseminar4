from random import randint as rnd

def PoliModel (min: int, max: int,poliNnumber:str) -> dict:
    print("Введите степень",poliNnumber ," полинома : ")
    degree = int(input())
    model = {}
    for key in range(degree, -1, -1):
        value = rnd(min, max)
        model[key] = value
    return model


def CreatePolinom(polinom: dict) -> str:
    newPolinom= ''
    flag = True
    for (key, value) in polinom.items():
        if value != 0:
            if flag:
                if value > 0:
                    newPolinom+= f'{value}*x**{key} '
                else:
                    newPolinom+= f'-{value * (-1)}*x**{key} '
                flag = False
            else:
                if value == 1:
                    if key == 1:
                        newPolinom+= f'+ x '
                    elif key == 0:
                        newPolinom+= f'+ 1 '
                    else:
                        newPolinom+= f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        newPolinom+= f'+ {value}*x '
                    elif key == 0:
                        newPolinom+= f'+ {value} '
                    else:
                        newPolinom+= f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        newPolinom+= f'- x '
                    elif key == 0:
                        newPolinom+= f'- 1 '
                    else:
                        newPolinom+= f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        newPolinom+= f'- {abs(value)}*x '
                    elif key == 0:
                        newPolinom+= f'- {abs(value)} '
                    else:
                        newPolinom+= f'- {abs(value)}*x**{key} '
    return newPolinom+ '= 0'


def SplitPolinom(polinom: str) -> dict:
    newPolinom= []
    polinom = polinom.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in polinom:
        if not 'x' in item:
            newPolinom.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    newPolinom.append(['1', '1'])
                elif item == '-x':
                    newPolinom.append(['-1', '1'])
                else:
                    newPolinom.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    newPolinom.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    newPolinom.append(item.replace('-', '-1').split('x**'))
                else:
                    newPolinom.append(item.split('*x**'))
    model = {}
    for item in newPolinom:
        model[int(item[1])] = int(item[0])
    return model


poliFirst = PoliModel(-100, 100,"первого")
poliSecond = PoliModel(-100, 100,"второго")

def PoliSum(first: dict, second: dict) -> dict:
    base = {}
    base.update(poliFirst)
    base.update(poliSecond)
    for key in base:
        if poliFirst.get(key) and poliSecond.get(key):
            base[key] = poliFirst.get(key) + poliSecond.get(key)
        elif poliFirst.get(key):
            base[key] = poliFirst.get(key)
        else:
            base[key] = poliSecond.get(key)
    return dict(sorted(base.items())[::-1])

result = PoliSum(poliFirst, poliSecond)
print("Первый многочлен :")
print(CreatePolinom(poliFirst))
print("Второй многочлен :")
print(CreatePolinom(poliSecond))
print("Сумма многочленов :")
print(CreatePolinom(result))
