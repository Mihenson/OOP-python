import csv

class Record():
    idx = 0
    
    def __init__(self, idx: int):
        self.__setattr__("idx", idx)
        

# Класс наследуемый от класс Record, который содержить в себе атрибут Record и имеет свои атрибуты
class RecordStrings(Record):
    idx = 0
    nickname = ""
    text = ""
    likes = 0

    # Атрибуты иницилизируются только с помощью __setatter__
    def __init__(self, idx: int, nickname: str, text: str, likes: int):
        super().__init__(idx)
        self.__setattr__('text', text)
        self.__setattr__('nickname', nickname)
        self.__setattr__('likes', likes)

    # Налсожение ограничений на __setatter__, чтобы не создавать лишние атрибуты
    def __setattr__(self, key, value):
        if not(key in ['idx', 'nickname', 'text', 'likes']):
            raise KeyError("Нет такого атрибута")
        else:
            self.__dict__[key] = value

    # Пример распределенея стандартного метода
    def __repr__(self):
        return f"RecordStrings(idx={self.idx}, nickname={self.nickname}, " \
               f"text={self.text}, likes={self.likes})"
class Data():
    path = ""
    table = []
    item = 0

    def __init__(self, path):
        self.path = path
        self.table = self.parse(self.path)

    def __iter__(self):
        return self

    # Функция класса для добавление новой записи в таблицу. Всё то же, что и в 3 работе
    def add_new_record(self):
        new_record = RecordStrings(int(input("Номер поста: ")), input("Никнейм: "), input("Текст: "), int(input("Количество лайков: ")))
        with open(self.path, "a") as f:
            writer = csv.DictWriter(f, fieldnames=['idx', 'nickname', 'text', 'likes'])
            writer.writerow(new_record.__dict__)
        f.close()

        self.table = self.parse(self.path)

    # Реализация генератора
    def my_generator(self):
        self.item = 0

        while self.item < len(self.table):
            yield self.table[self.item]
            self.item += 1

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.table]})"

    # Реализация функции __next__
    def __next__(self):
        if self.item >= len(self.table):
            self.item = 0
            raise StopIteration
        else:
            self.item += 1
            return self.table[self.item - 1]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")

        if 0 <= item < len(self.table):
            return self.table[item]
        else:
            raise IndexError("Выход за границы списка.")

    def __str__(self):
        table_str = '\n'.join([str(rh) for rh in self.table])
        return f"Записи:\n{table_str}"

    @staticmethod
    # Функция для разбиения таблицы на записи
    def parse(path):
        res = []
        with open(path, "r") as f:
            reader = csv.DictReader(f, fieldnames=['idx', 'nickname', 'text', 'likes'])
            for record in reader:
                res.append(dict(record))
        f.close()

        return res

    # Сортировка различные варианты
    def my_sort(self, way_sort):
        if way_sort == 0:
            self.table.sort(key=lambda x: int(x['idx']))  # Сортировка по id
        elif way_sort == 1:
            self.table.sort(key=lambda x: x['nickname'])  # Сортировка по нику
        elif way_sort == 2:
            self.table.sort(key=lambda x: x['text'])  # Сортировка по тексту
        elif way_sort == 3:
            self.table.sort(key=lambda x: x['likes'])  # Сортировка по лайкам
        else:
            print("Такого метода сортировки нет")



if __name__ == "__main__":
    d = Data("lab4.csv")

    print("1. Класс должен содержать итератор:\n")
    for i in d.__iter__():
        print(i)

    print("\n2. Должна быть реализована перегрузка стандартных операций: \n")
    print(d.__repr__())
    print(d.__str__())

    print("\n3. Должно быть реализовано наследование:\nКласс RecordStrings наследуется от Record\n")

    print("\n4. Запись значений в свойства - только через __setattr__:\nСмотреть выше в коде\n")

    print("\n5. Возможность доступа к элементам коллекции по индексу (__getitem__):\n")
    print(d.__getitem__(1))

    print("\n6. Должны быть реализованы статические методы: \nСмотреть выше в коде\n")

    print("\n7. Должны быть реализованы генераторы\n")
    for i in d.my_generator():
        print(i)

    WRITE_RECORD = False  # Сделать запись в csv файл
    OUTPUT_RECORDS = True  # Вывести записи, выбрав сбособ сортировки
    SELECT_RECORDS = True  # Вывести записи по одному из критериев

    if WRITE_RECORD:
        d.add_new_record()

    if OUTPUT_RECORDS:
        print("Отсоритровать записпи по\n0 - id\n1 - нику\n"
              "2 - тексту\n3 - лайкам\n")
        way = int(input())
        d.my_sort(way)

        for line in d.table:
            print(line)

    if SELECT_RECORDS:
        print("\nБольше сотни лайков в этих постах:\n")
        for line in d.table:
            if (int(line['likes']) > 100):
                print(line)
input()
