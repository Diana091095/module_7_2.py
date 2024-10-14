from pprint import pprint


def custom_write(file_name, strings):
    """ file_name - название файла для записи, strings - список строк для записи."""
#     Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#   Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
#   а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью

    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    for num, stroc in enumerate(strings):
        cursor = file.tell()
        file.write(stroc + '\n')
        strings_positions[(num + 1, cursor)] = stroc

    return strings_positions
    file.close()



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

    # for i in range(len(strings)):
    #     cursor = file.tell()
    #     strings_positions = (i+1, strings)
    #     file.close()
    #     return strings_positions



    # file.write(strings + '\n')





