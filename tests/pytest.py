import pytest
import tempfile
import os
from main import main


class TestInputValidation:
    """Тесты валидации входных параметров"""

    def test_missing_files_parameter(self):
        """Тест на отсутствие параметра --files"""
        with pytest.raises(SystemExit):
            main(['--report', 'report.txt'])

    def test_missing_report_parameter(self):
        """Тест на отсутствие параметра --report"""
        with pytest.raises(SystemExit):
            main(['--files', 'file1.txt', 'file2.txt'])

    def test_nonexistent_files(self):
        """Тест с несуществующими файлами"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as report_file:
            report_path = report_file.name

        try:
            with pytest.raises(SystemExit):
                main(['--files', 'nonexistent1.txt', 'nonexistent2.txt',
                      '--report', report_path])
        finally:
            os.unlink(report_path)