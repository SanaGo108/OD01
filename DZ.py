# Шаг 1: Преобразовать строку в нижний регистр, чтобы игнорировать регистр символов
# Шаг 2: Удалить из строки все пробелы и, если необходимо, другие неалфавитные символы
# Шаг 3: Определить длину строки
# Шаг 4: Использовать цикл для сравнения символов с начала и конца строки
# Шаг 5: Если символы не равны, строка не является палиндромом
# Шаг 6: Если все сравнения завершились успешно, строка является палиндромом
# Пример использования функции

def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

print(is_palindrome("A man, a plan, a canal, Panama"))  # Выводит: True
print(is_palindrome("Hello"))  # Выводит: False