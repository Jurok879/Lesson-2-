numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                            # создаем пустой список для простых чисел
not_primes = []                        # создаем пустой список для остальных чисел
for i in numbers:                      # перебираем список
    if i == 1:                         # исключаем "1", она не является ни простым ни состовным числом
        continue
    is_primes = True                   # согласно условия вводим переменную с флагом
    for j in range(2, i):              # перебираем по диапазону от "2" до "i"
        if i % j == 0:                 # условие проверки кратности
            is_primes = False
            break                      # конец цикла
    if is_primes:
        primes.append(i)               # если число простое, то добавляем в список "primes"
    else:
        not_primes.append(i)           # если число составное, то в список "not_primes"
print(primes)
print(not_primes)

