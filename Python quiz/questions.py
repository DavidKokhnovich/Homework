class Questions:
    def __init__(self):
        self.questions_list = [
            {"question": "Что такое Python?", "answer": "Язык программирования"},
            {"question": "Кто разработал Python?", "answer": "Гвидо ван Россум"},
            {"question": "Когда был выпущен Python 3.0?", "answer": "2008"},
            {"question": "Как расшифровывается ООП?", "answer": "Объектно-Ориентированное Программирование"},
            {"question": "Какое расширение у Python файлов?", "answer": ".py"},
            {"question": "Что такое библиотека в Python?", "answer": "Набор модулей"},
            {"question": "Какое ключевое слово используется для создания функции?", "answer": "def"},
            {"question": "Что такое список в Python?", "answer": "Коллекция упорядоченных элементов"},
            {"question": "Как сделать вывод в консоль?", "answer": "print()"},
            {"question": "Что такое pip?", "answer": "Менеджер пакетов для Python"},
        ]

    def get_random_question(self):
        import random
        return random.choice(self.questions_list)
