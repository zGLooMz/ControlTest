import Note


def write_file(array, mode):
    file = open("Test/Phyton/notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("Test/Phyton/notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close


def read_file():
    try:
        array = []
        file = open("Test/Phyton/notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array
