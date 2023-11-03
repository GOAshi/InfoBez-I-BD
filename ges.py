#СУММА ТРЁХ ЧИСЕЛ
a=int(input())
b=int(input())
c=int(input())
print(a+b+c)

КУБ
x=int(input())
print('Объём=',x*x*x)
print('Площадь полной поверхности=', 6*x*x)

#ЗНАЧЕНИЕ ФУНКЦИИ
a=int(input())
b=int(input())
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41)

#СЛЕДУЮЩЕЕ И ПРЕДЫДУЩЕЕ
score=int(input())
print('Следующее за числом',score,'число:',score+1)
print('Для числа',score,'Предыдущее число:',score-1)

#СТОИМОСТЬ ПОКУПКИ
x=int(input())
y=int(input())
z=int(input())
c=int(input())
print(3*(x+y+z+c))

#АРИФМЕТИЧЕСКАЯ ОПЕРАЦИЯ
a=int(input())
b=int(input())
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)

#АРИФМЕТИЧЕСКАЯ ПРОГРЕССИЯ
a=int(input())
b=int(input())
c=int(input())
x=a+b*(c-1)
print(x)

#РАЗДЕЛЯЙ И ВЛАСТВУЙ
x=int(input())
print(x,2*x,3*x,4*x,5*x, sep='---')

#ГЕОМЕТРИЧЕСКАЯ ПРОГРЕССИЯ
a=int(input())
b=int(input())
c=int(input())
x=a*b*((c-1)*2)
print(x)

#РАССТОЯНИЕ В МЕТРАХ
a=int(input())
print('В', a, 'сантиметрах',a%1000//100,'метра')

#МАНДАРИНЫ
a=int(input())
b=int(input())
print(b//a)
print(b%a)

#САМА НЕОТВРАТИМОСТЬ
a=int(input())
if a%2==0:
    print(a//2)
else:
    print(a//2+1)

#НОМЕР КУПЕ
a=int(input())
print(a//4+1)

#ПЕРЕСЧЕТ ВРЕМЕННОГО ИНТЕРВАЛА
a=int(input())
print(a,'мин','-','это',a//60,'час',a%60,'минут')

#ТРЕХЗНАЧНОЕ ЧИСЛО
a=int(input())
a1=a//100
a2=a%100//10
a3=a%10
print('Сумма цифр=',a1+a2+a3)
print('Произведение цифр=',a1*a2*a3)

#ПЕРЕСТАНОВКА ЦИФР
n=int(input())
a=n//100
b=n%100//10
c=n%10
print(a,b,c,sep='')
print(a,c,b,sep='')
print(b,a,c,sep='')
print(b,c,a,sep='')
print(c,a,b,sep='')
print(c,b,a,sep='')

#ЧЕТЫРЕХЗНАЧНОЕ ЧИСЛО
a=int(input())
print('Цифра в позиции тысяч равна',a//1000)
print('Цифра в позиции сотен равна',a%1000//100)
print('Цифра в позиции десятков равна',a%100//10)
print('Цифра в позиции единиц равна',a%10)

#ПАРОЛЬ
a=int(input())
b=int(input())
if a==b:
    print('Пароль принят')
else:
    print('Пароль не принят')

#ЧЕТНОЕ ИЛИ НЕЧЕТНОЕ
a = int(input())

if a % 2:
    print('нечётное')
else:
    print('чётное')

#СООТНОШЕНИЕ
a=int(input())
if a//1000+a%10==a%1000//100-a%100//10:
    print('YES')
else:
    print('NO')

#РОСКОМНАДЗОР
a=int(input())
if a<18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')

#АРИФМЕТИЧЕСКАЯ ПРОГРЕССИЯ


#НАИМЕНЬШЕЕ ИЗ ДВУХ ЧИСЕЛ


#НАИМЕНЬШЕЕ И ЧЕТЫРЁХ ЧИСЕЛ


#ВОЗРАСТНАЯ ГРУППА


#ТОЛЬКО+
