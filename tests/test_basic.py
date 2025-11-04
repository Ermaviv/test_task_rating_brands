import pytest

from main import write_count_data


class TestWorkProgram:
    """Тест работоспособности программы"""

    def test_basic(self, generate_check_file):
        assert [row for row in open(r'.\tests\check_file')] == [row for row in open(r'.\tests\control_file')]

    def test_short_1(
            self,
            name_report_file,
            title_data,
            combining_data_1,
            expected_result_1,
    ):
        assert write_count_data(
            name_report_file(),
            combining_data_1(),
            title_data()
        ) == expected_result_1()

    def test_short_2(
            self,
            name_report_file,
            title_data,
            combining_data_2,
            expected_result_2
    ):
        assert write_count_data(
            name_report_file(),
            combining_data_2(),
            title_data()
        ) == expected_result_2()
