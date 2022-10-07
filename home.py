a = float(input('Введите значение a:'))
b = float(input('Введите значение b:'))
c = float(input('Введите значение c:'))

D = b**2 - 4*a*c

x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)

if D < 0:
    print('Нет корней')
elif D == 0:
    print(x1)
else:
    print(x1,x2)