# "Базовые структуры данных"
#----------------------------------------------
# Старая версия.
# Ссылка на старую версию тут

# "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5,
# после умножение на 5.
print(9**0.5*5)

# "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно.
print(9.99>9.98 and 1000<1000.1)

# "3rd program".
# Дано два целых четырёхзначных числа: 1234 и 5678.
# Выведите на экран(в консоль) сумму серединных чисел исходных данных (23 и 67).
print(1234%1000//10+5678%1000//10)

#"4th program"
# Дано два дробных числа: 13.42 и 42.13.
# Необходимо убедиться в том, что целая часть хотя бы одного из чисел
# равна дробной части другого. Например: 13 == 13 (13.42, 42.13) или 42 == 42 (13.42, 42.13).
print(13.42//1==42.13*100%1000%100 or 42.13//1==13.42*100%1000%100 )