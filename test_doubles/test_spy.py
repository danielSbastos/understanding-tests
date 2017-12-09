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

from unittest.mock import MagicMock

def test_with_spy():
    street = MagicMock()
    street.get_description.return_value = 'Max Colin'

    jlle_1 = Joinville('América', street)
    jlle_2 = Joinville('Atiradores', street)

    str(jlle_1)
    str(jlle_2)

    assert street.get_description.call_count == 2
