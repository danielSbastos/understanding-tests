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

class StreetFake:
    STREET = 'Max Colin'

    def get_description(self):
        return self.STREET

def test_with_fake():
    street = StreetFake()
    jlle = Joinville('América', street)

    assert str(jlle) == 'Neighborhood: América, Street: Max Colin'
