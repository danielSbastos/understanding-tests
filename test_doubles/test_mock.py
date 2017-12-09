from unittest.mock import MagicMock

class Joinville:
    POPULATION = 569645

    def __init__(self, neighborhood, street):
        self.neighborhood = neighborhood
        self.street = street

    def __str__(self):
        return "Neighborhood: %s, Street: %s" % (
            self.neighborhood,
            self.street.get_description(),
        )


# Test

def test_with_mock():
    street = MagicMock()
    street.get_description.return_value = 'Max Colin'
    jlle = Joinville('América', street)

    assert str(jlle) == 'Neighborhood: América, Street: Max Colin'
    street.get_description.assert_called_once_with()
