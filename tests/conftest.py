import pytest
from main import main


@pytest.fixture()
def title_data():
    return ['name', 'brand', 'price', 'rating']


@pytest.fixture()
def name_report_file():
    return 'report_file'


@pytest.fixture()
def title_data():
    return ['name', 'brand', 'price', 'rating']


@pytest.fixture()
def combining_data_1():
    return {'apple': [4.9, 4.7]}


@pytest.fixture()
def combining_data_2():
    return {
        'brand_1': [3.9, 3.7],
        'brand_2': [1],
        'brand_3': [4.9, 4.7, 4.8],
    }


@pytest.fixture()
def expected_result_1():
    return [
        ['', 'brand', 'rating'],
        [1, 'apple', 4.8],
    ]


@pytest.fixture()
def expected_result_2():
    return [
        ['', 'brand', 'rating'],
        [1, 'brand_3', 4.8],
        [1, 'brand_1', 3.8],
        [3, 'brand_2', 1],
    ]


'''
@pytest.fixture()
def cmd_output():
    output = subprocess.run(
        [
            'python', 'main.py', '--files', 'products1.csv', 'products2.csv',
            '--report', 'average-rating'
        ],
        capture_output=True, text=True
    )
    return output.stdout
'''


@pytest.fixture
def generate_check_file():
    main(
        ['--files', 'products1.csv', 'products2.csv',
         '--report', r'.\tests\check_file']
    )


'''
@pytest.fixture()
def control_file():
    return [
        ['', 'brand', 'rating'],
        [1, 'apple', 4.55],
        [2, 'samsung', 4.53],
        [3, 'xiaomi', 4.37]
    ]
'''
