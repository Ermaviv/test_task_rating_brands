"""Модуль для вычисления среднего рейтинга."""
import argparse
import csv
import os
import sys
from tabulate import tabulate


def main(cmd_data):
    """Главный файл."""
    validate_data(cmd_data)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Список файлов для обработки'
    )
    parser.add_argument(
        '--report',
        nargs=1,
        required=True,
        help='Укажите, куда загрузить результаты'
    )
    arg = parser.parse_args(cmd_data)
    content, title = combining_data(arg)
    return write_count_data(*arg.report, content, title)


def combining_data(args):
    """Сбор и группировка рейтингов."""
    content = {}
    if args.files:
        for file_name in args.files:
            try:
                with open(file_name, 'r', encoding='utf8') as file:
                    current_file_content = list(csv.reader(file))
                    title = current_file_content[0]
                    for string in current_file_content:
                        if string == title:
                            continue
                        validate_string(string)
                        if string[1] not in content.keys():
                            content[string[1]] = [
                                float(string[len(title) - 1])
                            ]
                        else:
                            content[string[1]].append(
                                float(string[len(title) - 1])
                            )
            except FileNotFoundError:
                print(f"Ошибка: файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при чтении {file_name}: {str(e)}")
    else:
        print("Файлы не указаны."
              "Укажите в формате python main.py --files"
              "<файлы со студентами> -- report <куда написать>"
              )
    return [content, title]


def write_count_data(report_file, content, title):
    """Подсчет и запись файлов."""
    with open(report_file, 'w', encoding='utf8') as write_file:
        writer = csv.writer(write_file)
        content_item = []
        numerate_list = [['', title[1], title[len(title) - 1]]]
        writer.writerow(['', title[1], title[len(title) - 1]])

        for name, marks in content.items():
            content[name] = round(sum(marks) / len(content[name]), 2)
            content_item.append([name, content[name]])
        content_item.sort(key=lambda x: -x[1])
        for count, name_marks in enumerate(content_item, 1):
            name, marks = name_marks
            numerate_list.append([count, name, marks])
            writer.writerow([count, name, marks])
        headers = numerate_list.pop(0)
        write_file.close()
        return tabulate(numerate_list, headers, tablefmt="pretty")


def validate_data(data):
    """Валидация запроса."""
    length = len(data)
    if length <= 3:
        raise ValueError("There are must be at least 4 values"
                         "(get %d) like"
                         "--files <name_file_with_table>"
                         "--report <name_file_for_report>" % length)
    try:
        if data[0] != '--files':
            raise ValueError("First parameter must be '--files'.")
        if data[length - 2] != '--report':
            raise ValueError("parameter '--report'"
                             "must have a name of only 1 file.")
        number_files = length - 3
        for i in range(1, number_files):
            file_path = data[i]
            if not os.path.exists(file_path):
                raise ValueError(f"Файл {file_path} не существует.")
    except Exception as e:
        raise e


def validate_string(string):
    """Построчная валидация строк входных файлов."""
    if float(string[2]) < 0:
        raise ValueError("string %d has invalid price.", string)
    if float(string[3]) < 0:
        raise ValueError("string %d has invalid rating.", string)


if __name__ == "__main__":
    sys.exit(print(main(sys.argv[1:])))
