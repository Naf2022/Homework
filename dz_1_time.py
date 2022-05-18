print('Hello World!')

#DZ: Реализовать вывод информации о промежутке времени в зависимости от его
#продолжительности duration в секундах:
#a. до минуты: <s> сек;
#b. до часа: <m> мин <s> сек;
#c. до суток: <h> час <m> мин <s> сек;
#d. * в остальных случаях: <d> дн <h> час <m> мин <s> .
day_seconds = 86400
hours_seconds = 3600
minutes_seconds = 60
time = ()

# выводим только секунды,т.к. меньше 60.*
time = int(input('Введите время в секундах: '))
if time < 60 :
    print(time, 'сек.')

#выводим только минуты и секунды:
elif time <= 3599:
    minutes = time // minutes_seconds
    seconds_rest = time % minutes_seconds
    print(minutes,'мин',seconds_rest,'сек')

#выводим только часы, минуты и секунды:
elif time <= 86399:
    hours = time // hours_seconds
    minutes_rest = int(time % hours_seconds)
    minutes = minutes_rest // minutes_seconds
    seconds_rest = minutes_rest % minutes_seconds
    print(hours,'чc ', minutes, 'мин ', seconds_rest,'сек')

#все остальные случаи:
elif time > 86399:
    days = time // day_seconds
    days_rest = int(time % day_seconds)
    hours = days_rest // hours_seconds
    hours_rest = int(days_rest % hours_seconds)
    minutes = hours_rest // minutes_seconds
    seconds = int(minutes % minutes_seconds)
    print(days, 'дн', hours, 'чc', minutes, 'мин', seconds,'сек')






