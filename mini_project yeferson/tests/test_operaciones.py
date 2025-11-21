from mini_proyecto.operaciones import Cajero
import pytest

def test_depositar():
    c = Cajero(1000)
    assert c.depositar(500) == 1500

def test_retirar():
    c = Cajero(1000)
    assert c.retirar(300) == 700

def test_retirar_sin_fondos():
    c = Cajero(500)
    with pytest.raises(ValueError):
        c.retirar(600)
