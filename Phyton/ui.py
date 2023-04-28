import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nПрограмма 'Заметки' Имеет следующие функции:\n\n1 - Вывод всех заметок из файла\n2 - Добавление заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выборка заметок по дате\n6 - Вывод заметки по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть более {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Работа программы завершена")
