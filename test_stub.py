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

from unittest.mock import MagicMock

def test_usando_stub():
    rua = MagicMock()
    rua.get_descricao.return_value = 'Max Colin'
    jlle = Joinville('América', rua)

    assert str(jlle) == 'Bairro: América, Rua: Max Colin'
