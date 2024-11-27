#5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial(number):
    # проверяем, равно ли число нулю
    if number == 0:
        return 1
    # создаём переменную для хранения результата
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(7))