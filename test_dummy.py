class Joinville:
    POPULACAO = 569645

    def __init__(self, bairro, rua):
        self.bairro = bairro
        self.rua = rua

# Teste

def test_usando_dummy():
    rua = None
    jlle = Joinville('América', rua)

    assert jlle.POPULACAO == 569645
