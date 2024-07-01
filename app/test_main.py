import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected, url",
    [
        (True, True, "Accessible", "https://translate.google.com/"
                                   "?hl=ru&sl=en&tl=ru&op=translate"),
        (False, True, "Not accessible", ""),
        (True, False, "Not accessible", "https://translate.google.com/?hl="
                                        "ru&sl=en&tl=ru&op=translate")
    ]
)
def test_can_access_google_page(valid_url: bool, internet_connection: bool,
                                expected: str, url: str) -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=valid_url),
        mock.patch("app.main.has_internet_connection",
                   return_value=internet_connection)
    ):
        assert can_access_google_page(url) == expected
