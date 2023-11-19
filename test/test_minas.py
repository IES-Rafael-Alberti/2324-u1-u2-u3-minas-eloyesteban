from src.minas  import ( colocar_minas, inicializar_tablero)

def test_colocar_minas():
    filas, columnas = 5, 5
    num_minas = 5
    minas = colocar_minas(filas, columnas, num_minas)

    assert len(minas) == num_minas
    for mina in minas:
        assert 0 <= mina[0] < filas
        assert 0 <= mina[1] < columnas



def test_inicializar_tablero():
    filas, columnas, num_minas = 5, 5, 5
    tablero_real, tablero_visible, celdas_destapadas, minas = inicializar_tablero(filas, columnas, num_minas)

    assert len(minas) == num_minas
    assert len(tablero_real) == filas
    assert len(tablero_real[0]) == columnas
    assert len(tablero_visible) == filas
    assert len(tablero_visible[0]) == columnas
    assert len(celdas_destapadas) == 0

