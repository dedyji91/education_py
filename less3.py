#Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.

#Получаемое число A всегда меньше либо равно B.

#На вход программе в три строки подаются переменные в следующем порядке: A, B, H.

#Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании,
#т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.

#Это первое не самое тривиальное задание на условное выражение. В случаях, когда разбить исполнение программы на несколько направлений,
#стоит внимательно обдумать все условия, которые нужно использовать. Особое внимание стоит уделить строгости используемых условных операторов: различайте < и ≤; > и ≥.
#Для того, чтобы понимать, какой из них стоит использовать, внимательно прочитайте условие задания.

#Sample Input 1:
#6
#10
#8
#Sample Output 1:
#Это нормально

#Sample Input 2:
#7
#9
#10
#Sample Output 2:
#Пересып

#Sample Input 3:
#7
#9
#2
#Sample Output 3:
#Недосып


a = int(input('Enter A: '))
b = int(input('Enter B: '))
h = int(input('Enter H: '))
if a <= b == h:
    print('Это нормально')
elif a <= b < h:
    print('Пересып')
elif a <= b > h:
    print('Недосып')


