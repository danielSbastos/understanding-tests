class Joinville:
    POPULATION = 569645

    def __init__(self, neighborhood, street):
        self.neighborhood = neighborhood
        self.street = street


# Test

def test_with_dummy():
    street = None
    jlle = Joinville('América', street)

    assert jlle.POPULATION == 569645


