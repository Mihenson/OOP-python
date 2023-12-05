import csv

mydicts = []        # Словарь
path = "data.csv"

# Сортировка различные варианты
def my_sort(mydicts, way_sort):
    if way_sort == 0:
        mydicts.sort(key=lambda x: int(x['id']))       # Сортировка по id
    elif way_sort == 1:
        mydicts.sort(key=lambda x: x['nick'])        # Сортировка по нику
    elif way_sort == 2:
        mydicts.sort(key=lambda x: x['text'])         # Сортировка по тексту
    elif way_sort == 3:
        mydicts.sort(key=lambda x: x['likes'])         # Сортировка по лайкам
    else:
        print("Такого метода сортировки нет")
        quit()


# Функция для вывода записи
def format_print_dict(line):
    print(f"\nID - {line['id']}:"
          f"\nNikcname - {line['nick']}"
          f"\nText - {line['text']}"
          f"\nLikes - {line['likes']}")


# Рычаги для управления программы
GET_COUNT_FILE_DIR = False      # Считать файлы в директории
WRITE_RECORD = True            # Сделать запись в csv файл
LOAD_RECORDS = True        # Загрузить записи
OUTPUT_RECORDS = False          # Вывести записи, выбрав сбособ сортировки. LOAD_RECORS должен быть True
SELECT_RECORDS = False       # Вывести записи по одному из критериев. LOAD_RECORS должен быть True
if __name__ == "__main__":

    if GET_COUNT_FILE_DIR:
        try:
            path = input("Введите путь директории(папки): ")
            # root - имя корневого каталога
            # dirs - список имен вложенных папок
            # files - список файлов в текущем каталоге
            root, dirs, files = next(os.walk(path))     # Выдаёт тройной кортеж - (dirpath, dirnames, filenames)
                                                        # возвращающает имена файлов в дереве каталогов, двигаясь по дереву сверху вниз
            print("Количество файлов в данной директории: ", len(files))
        except FileNotFoundError:
            print("Директория с таким путём не найдена...")
            quit()

    if WRITE_RECORD:
        idx = input("Номер поста: ")
        nick_name = input("Ник: ")
        post_text = input("Текст: ")
        count_likes = input("Количество лайков: ")
        
        line = {'id': idx, 'nick': nick_name, 'text': post_text, 'likes': count_likes}

        with open(path, "a", newline="") as file:
            writer = csv.DictWriter(file,  fieldnames=['id', 'nick', 'text', 'likes'])       # Объект писателя, с помощью которого и записываем файл
            writer.writerow(line)         # Сделать запись
            file.close()

    if LOAD_RECORDS:
        with open(path, "r") as tabel_file:
            reader = csv.DictReader(tabel_file, fieldnames=['id', 'nick', 'text', 'likes'])
            for record in reader:
                mydicts.append(dict(record))

        if OUTPUT_RECORDS:
            print("Отсоритровать записпи по\n0 - id\n1 - нику\n"
                  "2 - тексту\n3 - лайкам")
            way = int(input())
            my_sort(mydicts, way)

            for line in mydicts:
                format_print_dict(line)
        if SELECT_RECORDS:
            print("\nБольше сотни лайков в этих постах:\n")
            for line in mydicts:
                if(int(line['likes']) > 100):
                    format_print_dict(line)

        
input()                    
