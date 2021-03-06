#task1----------------------------------------------------
"""
По данному целому числу N распечатайте все квадраты натуральных чисел,
не превосходящие N, в порядке возрастания.
"""
n = int(input())
i = 1
sqr = 1
while sq<=n:
    print(sq)
    i += 1
    sqr = i**2

#---------------------------------------------------------

#task2----------------------------------------------------
"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный
делитель, отличный от 1.
"""
num = int(input())
i = 2
while num % i != 0:
	i += 1
print(i)

#---------------------------------------------------------

#task3----------------------------------------------------
"""
По данному натуральному числу N найдите наибольшую целую степень двойки,
не превосходящую N. Выведите показатель степени и саму степень.
"""
i=1
power=0
n=int(input())
while n>=i*2:
    power+=1
    i=2*i
print(power, i)

#---------------------------------------------------------

#task4----------------------------------------------------
"""
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
"""
x = int(input())
y = int(input())
days = 1
while x < y:
    x += x * 0.1
    days += 1
print(days)

#---------------------------------------------------------

#task5----------------------------------------------------
"""
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов,
после чего дробная часть копеек отбрасывается. Определите,
через сколько лет вклад составит не менее y рублей.
Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей,
т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
"""
x = float(input())
p = float(input())
y = float(input())
z = x
i = 0
while z < y:
    z += z * p/100
    z = round(z, 2)
    i += 1
print(i)
#---------------------------------------------------------

#task6----------------------------------------------------
"""
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. 
Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу 
и вывести количество членов последовательности (не считая завершающего числа 0).
Числа, следующие за числом 0, считывать не нужно.
"""
count = 0
while int(input())!=0:
    count += 1
print(count)

#---------------------------------------------------------

#task7----------------------------------------------------
"""
Определите сумму всех элементов последовательности, завершающейся числом 0.
В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""
n = 1
sum = 0
while n!=0:
    n = int(input())
    sum += n
print(sum)

#---------------------------------------------------------

#task8----------------------------------------------------
"""
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""
i = 0
count = 0
while True:
    x = int(input(""))
    if x == 0:
        break
    i += x
    count += 1
print(i/count)
#---------------------------------------------------------

#task9----------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
"""
i = 0
max = 0
while True:
    x = int(input())
    if x == 0:
        break
    if max < x:
        max = x
print(max)

#---------------------------------------------------------

#task10----------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите индекс наибольшего элемента последовательности.
Если наибольших элементов несколько, выведите индекс первого из них. 
Нумерация элементов начинается с нуля.
"""
i = 0
max_el = 0
max_ind = 0
while True:
    x = int(input())
    if x == 0:
        break
    if max_el < x:
        max_el = x
        max_ind = i
    i += 1
print(max_ind)

#---------------------------------------------------------

#task11----------------------------------------------------
"""
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""
i = 0
evens = 0
while True:
    n = int(input(""))
    if n == 0:
        break
    if n%2 == 0:
        i += 1
print(i)


#---------------------------------------------------------

#task12----------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""
prev = int(input())
count = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        count += 1
    prev = next
print(count)

#---------------------------------------------------------

#task13----------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
"""
max = 0
list = []
x = 0
while True:
    x = int(input())
    list.append(x)
    if x == 0:
        break
list.sort()
print(list[-2])

#---------------------------------------------------------

#task14----------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""
n = int(input())
num = 1
max = n
while n!=0:
    n = int(input())
    if n == max:
        num += 1
    if n > max:
        max = n
        num = 1
print(num)

#---------------------------------------------------------


#task15----------------------------------------------------
"""
Последовательность Фибоначчи определяется так:
	φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.
"""
n = int(input())
if n == 0:
    print(0)
else:
    fib = []
    fib.append(0)
    fib.append(1)
    i = 2
    while i<=n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    print(fib[-1])

#---------------------------------------------------------

#task16----------------------------------------------------
"""
Дано натуральное число A.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φn = A. 
Если А не является числом Фибоначчи, выведите число -1.
"""
A = int(input())
if A == 0:
    print(0)
else:
    n1, n2 = 0, 1 
    i=1
    while n2<=A:
        if n2 == A:
            print(i)
            break
        n1, n2 = n2, n1 + n2
        i += 1
    else:
        print(-1)
#---------------------------------------------------------

#17---------------------------------------------------------
"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""
count = 1
max = 1 
a = int(input())
while a != 0:
    b = a
    a = int(input())
    if b == a:
        count += 1
    elif count > max:
        max = count
        count = 1
    else:
        count = 1
print(max)
----------------------------------------------------------
















