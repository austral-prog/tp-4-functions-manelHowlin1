# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    r1 = (-b+(b*b-4*a*c)**(1/2)) / (2*a)
    r2 = (-b-(b*b-4*a*c)**(1/2)) / (2*a)

    if r1 == r2:
        raiz = f"({r1})"
        return raiz
    elif (b*b - 4*a*c) < 0:
        return "( )"
    else:
        raices = f"({r1}, {r2})"
        return raices

def value_y(a, b, c, x):
    valor = int(a * x**2 + b * x + c)
    return valor



def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        funcion_string = f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0:
        if b != 0 and c != 0:
            funcion_string = f"f(x) = {b} * X + {c}"
        elif b == 0 and c != 0:
            funcion_string = f"f(x) = {c}"
        elif b == 0 and c == 0:
            funcion_string = f"f(x) = 0"
        elif b != 0 and c == 0:
            funcion_string = f"f(x) = {b} * X"
    elif b == 0:
        if c != 0:
            funcion_string = f"f(x) = {a} * X^2 + {c}"
        elif c == 0:
            funcion_string = f"f(x) = {a} *X^2"
    elif c == 0:
        funcion_string = f"f(x) = {a} * X^2 + {b} * X"
    return funcion_string


def derivation(a, b, c):
    if a != 0:
        if b != 0:
            derivada = f"f'(x) = {a*2} * X + {b}"
        elif b == 0:
            derivada = f"f'(x) = {a*2} * X"
    elif a == 0:
        if b != 0:
            derivada = f"f'(x) = {b}"
        elif b == 0:
            derivada = f"f'(x) = 0"
    return derivada
