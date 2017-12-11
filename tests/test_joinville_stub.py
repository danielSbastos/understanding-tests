from unittest.mock import MagicMock
from understanding_tests.joinville import Joinville


def test_with_stub():
    street = MagicMock()
    street.get_description.return_value = 'Max Colin'
    jlle = Joinville('América', street)

    assert str(jlle) == 'Neighborhood: América, Street: Max Colin'
