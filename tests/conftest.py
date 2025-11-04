import pytest

from main import main


@pytest.fixture()
def title_data():
    return ['name', 'brand', 'price', 'rating']


@pytest.fixture()
def headers():
    return ['', 'brand', 'rating']


@pytest.fixture()
def name_report_file():
    return 'report_file'


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
        [1, 'apple', 4.8],
    ]


@pytest.fixture()
def expected_result_2():
    return [
        [1, 'brand_3', 4.8],
        [2, 'brand_1', 3.8],
        [3, 'brand_2', 1.0],
    ]


@pytest.fixture
def generate_check_file():
    main(
        ['--files', 'products1.csv', 'products2.csv',
         '--report', r'.\tests\check_file']
    )
