# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----
    if is_even(n) and is_positive(n) and n != 0:
        return "positive even"
    elif is_even(n) and not is_positive(n) and n != 0:
        return "negative even"
    elif not is_even(n) and is_positive(n) and n != 0:
        return "positive odd"
    elif not is_even(n) and not is_positive(n) and n != 0:
        return "negative odd"
    else:
        return "zero"
