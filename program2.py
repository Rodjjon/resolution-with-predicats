def idenoptend(strok):
    mas = strok.split("+")
    for i in mas:
        while mas.count(i) != 1:
            mas.remove(i)
    sorted(mas)
    return "+".join(mas)

def rezol1(strok, masg):
    mas = strok.split("+")
    for i in mas:
        if len(i) == 5 and (i[1]+'('+i[3]+')') in mas:
            mas.remove(i)
            mas.remove(i[1]+'('+i[3]+')')
            if len(mas) > 0:
                print(strok, "преобразовалось в", "+".join(mas))
                return "+".join(mas)
            else:
                print(strok, "преобразовалось в ▯")
                masg.append("▯")
                return "▯"
        elif len(i) == 4 and "-" + i[0] + "(" + i[2] + ")" in mas:
            mas.remove(i)
            mas.remove("-" + i[0] + "(" + i[2] + ")")
            if len(mas) > 0:
                print(strok, "преобразовалось в", "+".join(mas))
                return "+".join(mas)
            else:
                print(strok, "преобразовалось в ▯")
                masg.append("▯")
                return "▯"
        for j in alfpropoz:
            if len(i) == 5 and i[1] + '(' + j + ')' in mas:
                print('В', strok, "переименовали пропозициональную переменную", j, "в", i[3], "получили:", strok.replace(j, i[3]))
                mas[mas.index((i[1]+'('+j+')'))] = (i[1]+'('+i[3]+')')
                rezol1(strok.replace(j, i[3]))
            if len(i) == 4 and '-' +i[0] + '(' + j + ')' in mas:
                print('В', strok, "переименовали пропозициональную переменную", j, "в", i[2], "получили:",strok.replace(j, i[2]))
                mas[mas.index('-' +i[0] + '(' + j + ')')] = '-' +i[0] + '(' + i[2] + ')'
                rezol1(strok.replace(j, i[3]))
    if len(mas) > 0:
        return ("+".join(mas))
    else:
        print(strok, "преобразвовалось в ▯")
        masg.append("▯")
        return 0

def rezolution(strok1, strok2, mas):
    mas1 = strok1.split("+")
    mas2 = strok2.split("+")
    for i in mas1:
        if len(i) == 5 and (i[1]+'('+i[3]+')') in mas2:
            mas1.remove(i)
            mas2.remove(i[1]+'('+i[3]+')')
            mas1 = mas1 + mas2
            if len(mas1) > 0:
                return "+".join(mas1)
            else:
                mas.append("▯")
                return "▯"
        elif len(i) == 4 and "-" + i[0] + "(" + i[2] + ")" in mas2:
            mas1.remove(i)
            mas2.remove("-" + i[0] + "(" + i[2] + ")")
            mas1 = mas1 + mas2
            if len(mas1) > 0:
                return "+".join(mas1)
            else:
                mas.append("▯")
                return "▯"
        for j in alfpropoz:
            if len(i) == 5 and i[1] + '(' + j + ')' in mas2:
                print('В', strok2, "переименовали пропозициональную переменную", j, "в", i[3], "получили: ", strok2.replace(j, i[3]))
                #mas2[mas2.index((i[1] + '(' + j + ')'))] = (i[1] + '(' + i[3] + ')')
                return j+i[3]
            if len(i) == 4 and '-' + i[0] + '(' + j + ')' in mas2:
                print('В', strok2, "переименовали пропозициональную переменную", j, "в", i[2], "получили: ", strok2.replace(j, i[2]))
                #mas2[mas2.index('-' + i[0] + '(' + j + ')')] = '-' + i[0] + '(' + i[2] + ')'
                return j+i[2]
    return 0

print("Формат ввода дизъюнктов A(x)+C(a); ... B(x); ИЛИ {A(x)+C(a); ... B(x)}")
strok = input("Введите множество дизъюнктов K = ")

mas = []
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ()abcdtxyz+-"
alfpropoz = "abcdt"
alfvesh = "xyz"
doper = ""
for i in strok:
    if i in alf:
        doper += i
    elif i == ';' or i == '}':
        mas.append(idenoptend(doper))
        doper = ""
sorted(mas, key=len,)
i = 0
while i < len(mas):
    dopmas = mas[i].split("+")
    for j in mas:
        if j != mas[i]:
            dopmas1 = j.split("+")
            for k in dopmas:
                if k in dopmas1:
                    mas.append(idenoptend("+".join(dopmas + dopmas1)))
                    print("{} и {} преобразовали в {}".format(mas[i], j, idenoptend("+".join(dopmas + dopmas1))))
                    mas.remove(mas[i])
                    mas.remove(j)
                    i = 0
                    break
                for d in alfpropoz:
                    if len(k) == 5 and "-{}({})".format(k[1], d) in dopmas1:
                        print("В {} переименовали пропозициональную переменную {} на {} и получили {}".format(j, d, k[3], j.replace(d, k[3])))
                        mas.remove(j)
                        mas.append(j.replace(d, k[3]))
                        i = 0
                        break
                    elif len(k) == 4 and "{}({})".format(k[0], d) in dopmas1:
                        print("В {} переименовали пропозициональную переменную {} на {} и получили {}".format(j, d, k[2], j.replace(d, k[2])))
                        mas.remove(j)
                        mas.append(j.replace(d, k[2]))
                        i = 0
                        break
    i += 1
i = 0

while i < len(mas):
    dop1 = mas[i]
    dop1 = rezol1(dop1, mas)
    if dop1 == mas[i]:
        if dop1 != 0:
            j = i + 1
            while j < len(mas):
                dop2 = mas[j]
                dop3 = rezolution(dop1, dop2, mas)
                if dop3 == 0:
                    dop3 = rezolution(dop2, dop1, mas)
                    if len(str(dop3)) == 2:
                        mas[i] = mas[i].replace(dop3[0], dop3[1])
                        i = -1
                        break
                elif len(str(dop3)) == 2:
                    mas[j] = mas[j].replace(dop3[0], dop3[1])
                    i = -1
                    break
                if dop3 != 0:
                    print(dop1, "и", dop2, "переобразовалось в", dop3)
                    mas[i] = ""
                    mas[j] = ""
                    dop4 = idenoptend(dop3)
                    if dop4 == dop3:
                        mas.append(dop3)
                    else:
                        print(dop3, 'преобразовалось в', dop4)
                        mas.append(dop4)
                    i = 0
                    break
                else:
                    j += 1
        else:
            mas[i] = ""
            i = 0
        i += 1
    else:
        mas[i] = ""
        i = 0
        mas.append(dop1)

while "" in mas:
    mas.remove("")
if mas.count("▯") > 0 and len(mas) > 0:
    print("Из множества", strok, "выводится пустая резольвента!🥳🥳🥳")
else:
    print("Из множества", strok, " НЕ выводится пустая резольвента!⚰️ ⚰️ ⚰️ ")
