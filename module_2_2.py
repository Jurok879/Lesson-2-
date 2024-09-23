first = 24
second = 42
third = 13

if first == second == third:                                  # если три числа равны
    print(3)
elif first == second or first == third or second == third:    # если два числа из трех равны
    print(2)
else:                                                         # если равных чисел нет
    print(0)
