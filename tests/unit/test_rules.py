from xm_demanda.quality.rules import clasificacion_es_coherente, valor_es_valido


def test_valor_negativo_no_es_valido():
    assert not valor_es_valido(-1.0)


def test_valor_nulo_no_es_valido():
    assert not valor_es_valido(None)


def test_regulado_debe_ser_sin_clasificar():
    assert clasificacion_es_coherente("Regulado", "SIN CLASIFICAR")
    assert not clasificacion_es_coherente("Regulado", "EDUCACIÓN")


def test_no_regulado_admite_ciiu():
    assert clasificacion_es_coherente("No Regulado", "EDUCACIÓN")
