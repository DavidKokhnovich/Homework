from datetime import datetime

books = []
readers = {}
loans = {}


def add_book(title, author, code):
    books.append({'title': title, 'author': author, 'code': code})

def register_reader(reader_id, last_name, first_name):
    if reader_id not in readers:
        readers[reader_id] = {'last_name': last_name, 'first_name': first_name, 'loans': []}
        print(f"Читатель {first_name} {last_name} зарегистрирован.")
    else:
        print("Читатель уже зарегистрирован.")

def loan_book(reader_id, book_code):
    if reader_id in readers and any(book['code'] == book_code for book in books):
        if book_code not in loans:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            loans[book_code] = {'reader_id': reader_id, 'date_issued': now, 'date_returned': None}
            readers[reader_id]['loans'].append(book_code)
            print(f"Книга с кодом {book_code} выдана читателю {readers[reader_id]['first_name']} {readers[reader_id]['last_name']}.")
            print(f"Дата выдачи книги: {now}")
        else:
            print("Книга уже выдана.")
    else:
        print("Читатель либо не зарегистрирован, либо книга не найдена.")

def return_book(reader_id, book_code):
    if book_code in loans and loans[book_code]['reader_id'] == reader_id:
        loans[book_code]['date_returned'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Дата возврата книги: {loans[book_code]['date_returned']}")
        readers[reader_id]['loans'].remove(book_code)
        del loans[book_code]
        print(f"Книга с кодом {book_code} возвращена.")
    else:
        print("Ошибка при возврате книги.")

def list_available_books():
    print("Доступные книги:")
    for book in books:
        if book['code'] not in loans:
            print(f"Код: {book['code']}, Название: {book['title']}, Автор: {book['author']}")
    if not any(book['code'] not in loans for book in books):
        print("Нет доступных книг.")

def main():

    # книги
    add_book("Война и мир", "Лев Толстой", "001")
    add_book("Маленький принц", "Антуан де Сент-Экзюпери", "002")
    add_book("Герой нашего времени", "Михаил Лермонтов", "003")

    while True:
        print("1. Регистрация читателя")
        print("2. Взять книгу")
        print("3. Вернуть книгу")
        print("4. Посмотреть доступные книги")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            reader_id = str(len(readers) + 1)
            print(f"Ваш ID: {reader_id}")
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            register_reader(reader_id, last_name, first_name)

        elif choice == '2':
            reader_id = input("Введите ID читателя: ")
            book_code = input("Введите код книги: ")
            loan_book(reader_id, book_code)

        elif choice == '3':
            reader_id = input("Введите ID читателя: ")
            book_code = input("Введите код книги: ")
            return_book(reader_id, book_code)

        elif choice == '4':
            list_available_books()

        elif choice == '5':
            print("Выход из системы.")
            break

        else:
            print("Недопустимый выбор. Попробуйте снова.")

print("Главное меню")
main()
