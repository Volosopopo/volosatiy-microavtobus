hours = int(input("Введите количество часов"))
b = int(input("Введите остаток по кредиту"))
c = int(input("Введите количество денег на еду"))
e = b + c
d = ((200*hours)/2**3) + hours
if d >= e:
    print("Часов хватает. Можно отдохнуть")
elif d<e:
    print("Часов не хватает. Придется работать")
a = 2.0
while a<=2.9:
    a = a + 0.1
    print(a)