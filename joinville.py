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
