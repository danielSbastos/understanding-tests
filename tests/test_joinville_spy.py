from unittest.mock import MagicMock
from understanding_tests.joinville import Joinville


def test_with_spy():
    street = MagicMock()
    street.get_description.return_value = 'Max Colin'

    jlle_1 = Joinville('América', street)
    jlle_2 = Joinville('Atiradores', street)

    str(jlle_1)
    str(jlle_2)

    assert street.get_description.call_count == 2
