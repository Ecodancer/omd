from unittest.mock import patch
from what_is_year_now import what_is_year_now


def test_get_year_format_ymd():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '2023-11-01'}
        assert what_is_year_now() == 2023
        mocked.assert_called_once()


def test_get_year_format_dmy():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '01.11.2023'}
        assert what_is_year_now() == 2023
        mocked.assert_called_once()


def test_get_exception():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '01@11@2023'}
        error = False
        try:
            what_is_year_now()
        except ValueError:
            error = True
        finally:
            assert error
        mocked.assert_called_once()
