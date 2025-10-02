import pytest
import subprocess


@pytest.fixture()
def first_file():
    file1 = [
        ['student_name', 'subject', 'teacher_name', 'date', 'grade'],
        ['Степанов Игорь', 'Биология', 'Ткаченко Наталья', '2023-11-18', 5],
        ['Чернова Виталина', 'Литература', 'Белова Светлана', '2023-11-20', 4],
        ['Иванов Алексей', 'Биология', 'Ткаченко Наталья', '2023-09-10', 2]
    ]
    return file1


@pytest.fixture()
def second_file():
    file2 = [
        ['student_name', 'subject', 'teacher_name', 'date', 'grade'],
        ['Иванов Алексей','Математика','Петрова Ольга','2023-09-10',5],
        ['Петрова Мария','Физика','Сидоров Иван','2023-09-12',4],
        ['Смирнов Дмитрий','Информатика','Козлов Андрей','2023-09-15',5]
    ]
    return file2


@pytest.fixture()
def expected_result():
    return [
        ['student_name', 'subject', 'teacher_name', 'date', 'grade'],
        ['Степанов Игорь', 5.0],
        ['Смирнов Дмитрий', 5.0],
        ['Чернова Виталина', 4.0],
        ['Петрова Мария', 4.0],
        ['Иванов Алексей', 3.5],
    ]


@pytest.fixture()
def cmd_output():
    output = subprocess.run(
        [
            'python', 'main.py', '--files', 'tests/students1.csv', 'tests/students1.csv',
            '--report', 'file_report'
        ],
        capture_output=True, text=True
    )
    return output.stdout
