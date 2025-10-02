import argparse
import csv
from tabulate import tabulate
import sys


def read_data(cmd_data):
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True, help='Список файлов для обработки')
    parser.add_argument(
        '--report',
        nargs=1,
        required=True,
        help='Укажите, куда загрузить результаты'
    )
    # return parser.parse_args(cmd_data)
    args, content, title = combining_data(parser.parse_args(cmd_data))
    print(write_data([args, content, title]))
    return 0


def combining_data(args):
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
                        if string[0] not in content.keys():
                            content[string[0]] = [int(string[4])]
                        else:
                            content[string[0]].append(int(string[4]))
            except FileNotFoundError:
                print(f"Ошибка: файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при чтении {file_name}: {str(e)}")
    else:
        print("Файлы не указаны."
              "Укажите в формате python main.py --files <файлы со студентами> -- report <куда написать>"
              )
    return [args, content, title]


def write_data(data):
    args, content, title = data
    with open(*args.report, 'w', encoding='utf8') as write_file:
        writer = csv.writer(write_file)
        content_item = []
        numerate_list = [['', title[0], title[4]]]
        writer.writerow(['', title[0], title[4]])

        for name, marks in content.items():
            content[name] = sum(marks) / len(content[name])
            content_item.append([name, content[name]])
        content_item.sort(key=lambda x: -x[1])
        for count, name_marks in enumerate(content_item, 1):
            name, marks = name_marks
            numerate_list.append([count, name, marks])
            writer.writerow([count, name, marks])
        headers = numerate_list.pop(0)
        write_file.close()
        return tabulate(numerate_list, headers, tablefmt="pretty")


if __name__ == "__main__":
    sys.exit(read_data(sys.argv[1:]))
