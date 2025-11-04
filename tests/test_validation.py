import pytest
import tempfile
import os
from main import main


class TestInputValidation:
    """Тесты валидации входных данных"""

    def test_miss_parameter_files(self):
        with pytest.raises(ValueError):
            main(['--report', 'report.txt'])

    def test_miss_parameter_report(self):
        with pytest.raises(ValueError):
            main(['--files', 'file1.txt', 'file2.txt'])

    def test_nonexistent_files(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as report_file:
            report_path = report_file.name
        try:
            with pytest.raises(ValueError):
                main(['--files', 'nonexistent1.txt', 'nonexistent2.txt',
                      '--report', report_path])
        finally:
            os.unlink(report_path)
