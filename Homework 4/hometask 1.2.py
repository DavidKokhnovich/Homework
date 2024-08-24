def prime_numbers(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    user_input = input("Введите число или 'exit' для завершения): ")

    if user_input.lower() == 'exit':
        print("Программа завершена.")
        break

    try:
        number = int(user_input)
        if prime_numbers(number):
            print(f"{number} - простое число.")
        else:
            print(f"{number} - не является простым числом.")
    except ValueError:
        print("Ошибка: Введите целое число или 'exit' для завершения.")