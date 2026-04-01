import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gastocerto import adicionar_gasto, listar_gastos, total_gastos, remover_gasto

ARQUIVO_TESTE = "gastos_teste.json"


@pytest.fixture(autouse=True)
def limpar_gastos(monkeypatch):
    monkeypatch.setattr("gastocerto.ARQUIVO", ARQUIVO_TESTE)
    yield
    if os.path.exists(ARQUIVO_TESTE):
        os.remove(ARQUIVO_TESTE)


def test_adicionar_gasto_valido():
    gasto = adicionar_gasto("Mercado", 150.0, "alimentação")
    assert gasto["descricao"] == "Mercado"
    assert gasto["valor"] == 150.0


def test_adicionar_gasto_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto("Erro", -10, "teste")


def test_adicionar_gasto_descricao_vazia():
    with pytest.raises(ValueError):
        adicionar_gasto("", 50.0, "teste")


def test_total_gastos():
    adicionar_gasto("Mercado", 100.0, "alimentação")
    adicionar_gasto("Ônibus", 50.0, "transporte")
    assert total_gastos() == 150.0


def test_remover_gasto():
    adicionar_gasto("Cinema", 40.0, "lazer")
    removido = remover_gasto(0)
    assert removido["descricao"] == "Cinema"


def test_remover_indice_invalido():
    with pytest.raises(IndexError):
        remover_gasto(99)