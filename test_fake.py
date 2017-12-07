class Joinville:
    POPULACAO = 569645

    def __init__(self, bairro, rua):
        self.bairro = bairro
        self.rua = rua

    def __str__(self):
        return "Bairro: {0}, Rua: {1}".format(
            self.bairro,
            self.rua.get_descricao(),
        )

# Teste

class RuaFake:
    RUA = 'Max Colin'

    def get_descricao(self):
        return self.RUA

def test_usando_fake():
    rua = RuaFake()
    jlle = Joinville('América', rua)

    assert str(jlle) == 'Bairro: América, Rua: Max Colin'
