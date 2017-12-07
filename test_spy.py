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

def test_usando_spy():
    rua = MagicMock()
    rua.get_descricao.return_value = 'Max Colin'

    jlle_1 = Joinville('América', rua)
    jlle_2 = Joinville('Atiradores', rua)

    str(jlle_1)
    str(jlle_2)

    assert rua.get_descricao.call_count == 2
