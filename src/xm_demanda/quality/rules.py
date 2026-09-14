"""Reglas de negocio del caso. Funciones puras: se prueban sin Spark."""

SIN_CLASIFICAR = "SIN CLASIFICAR"


def valor_es_valido(valor: float | None) -> bool:
    """La demanda y las pérdidas no pueden ser negativas ni nulas."""
    return valor is not None and valor >= 0


def clasificacion_es_coherente(tipo_mercado: str, clasificacion: str) -> bool:
    """En el mercado regulado la actividad económica siempre viene sin clasificar."""
    if tipo_mercado == "Regulado":
        return clasificacion == SIN_CLASIFICAR
    return True
