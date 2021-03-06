#task1------------------------------------------------------------
"""
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
"""



N=int(input()) 
a=1 
while a**2<=N: 
    print(a**2, end=" ") 
    a+=1

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

"""



N=int(input())
a=2
while N%a !=0:
  a+=1
print(a)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. 
Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
"""



N=int(input())
a=0
power_of_two=1
while (power_of_two*2)<n:
  i+=1
  power_of_two*=2
print(a, power_of_two)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
"""



x=int(input())
y=int(input())
a=1
first_run=x
while y>first_run:
  first_run+=first_run*0.1
  a+=1
print(a)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. 
Определите, через сколько лет вклад составит не менее y рублей.

Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей,
т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.

"""



x=float(input())
p=float(input())
y=float(input())
balance=x
a=0
while balance<y:
  balance+=balance*p/100
  palance=round(balance, 2)
  a+=1
rint(a)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество
членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.

"""



a=0
while True:
  n=int(input())
  if n==0
    break
  a+=1
print(a)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Определите сумму всех элементов последовательности, завершающейся числом 0.
В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""



a=0
while True:
  n=int(input())
  if n==0:
    break
  a+=n
print(a)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Определите среднее значение всех элементов последовательности, завершающейся числом 0.

"""


a=0
b=0
while True:
  n=int(input())
  if n==0:
    break
  a+=n
  b+=1
print(a/b)


#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
"""



a=0
max=0
while True:
  n=int(input())
  if n==0
    break
  if max<n:
    max=n
print(max)

#-----------------------------------------------------------------



#task10------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите индекс наибольшего элемента последовательности.
Если наибольших элементов несколько, выведите индекс первого из них.
Нумерация элементов начинается с нуля.

"""



a = 0
max = 0
max2 = 0
while True:
    n = int(input())
    if n == 0:
        break
    if max<n:
        max = n
        max2 = a
    a += 1
print(max2)

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, завершающейся числом 0.

"""



a=0
while True:
  n=int(input())
  if n==0:
    break
  if n%2==0:
    a+=1
print(a)

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""



amount=0
a=int(input())
while True:
   b=a
   a=int(input())
   if a==0:
       break
   if a>b:
       amount+=1
print(amount)

#-----------------------------------------------------------------



#task13------------------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
"""



a=int(input())
max=a
second_max=0
while a!=0:
    a=int(input())
    if a>max:
        second_max=max
        max=a
    if a>second_max and a<max:
        second_max=a
print(second_max)

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

"""



a=int(input())
amount=1
max=a
while a!=0:
    a=int(input())
    if a==max:
        amount+=1
    if a>max:
        max=a
        amount=1
print(amount)

#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for.
"""



a,b=0,1
n=int(input())
for i in range(1,n+1):
    a,b=b,a+b
print(a)

#-----------------------------------------------------------------



#task16------------------------------------------------------------
"""
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φn = A.
Если А не является числом Фибоначчи, выведите число -1.
"""



a=0
b=1
c=0
n=0
A=int(input())
while a<A:
    c=b
    b=a+b
    a=c
    n+=1
if a==A:
    print(n)
else:
    print("-1")

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

"""



amount=1
max=1
a=int(input())
while a!=0:
    b=a
    a=int(input())
    if b==a:
        amount+=1
    elif amount>max:
        max=amount
        amount=1
    else:
        amount=1
print(max)

#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""



import math
a=int(input())
amount=1
sum=a
res=0
square_sum=a*a
while a!=0:
    a=int(input())
    amount+=1
    sum+=a
    square_sum+=a*a
amount+=-1
s=sum/amount
res=math.sqrt((square_sum-2*s*sum+amount*s*s)/(amount-1))
print(res)

#-----------------------------------------------------------------
