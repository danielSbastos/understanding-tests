from understanding_tests.joinville import Joinville


class StreetFake:
    STREET = 'Max Colin'

    def get_description(self):
        return self.STREET

def test_with_fake():
    street = StreetFake()
    jlle = Joinville('América', street)

    assert str(jlle) == 'Neighborhood: América, Street: Max Colin'
