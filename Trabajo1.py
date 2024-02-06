from array import array;
import sympy as sp


f=array('f', [1.0,2.0,3.14,1,0,24,0.9,1999,5]);

def elem(A, i, j):
    """
    Función para obtener un elemento de una matriz 3x3 representada como un array.

    Parámetros:
    A (list): Array de 9 elementos de tipo flotante representando la matriz.
    i (int): Índice horizontal del elemento deseado (0, 1 o 2).
    j (int): Índice vertical del elemento deseado (0, 1 o 2).

    Retorna:
    float: El elemento en la posición (i, j) de la matriz.
    """
    if len(A) != 9:
        raise ValueError("El array debe tener 9 elementos.")

    if not (0 <= i < 3) or not (0 <= j < 3):
        raise ValueError("Los índices i y j deben estar en el rango [0, 2].")

    # Calculamos el índice correspondiente en el array unidimensional
    index = i * 3 + j

    return A[index]


def swap_rows(A, i, j):
    """
    Intercambia dos renglones de una matriz 3x3 representada como un array de una dimensión.

    Parámetros:
    A (array): Array de 9 elementos de tipo flotante representando la matriz.
    i (int): Índice del primer renglón.
    j (int): Índice del segundo renglón.

    Retorna:
    array: El array A con los renglones intercambiados.
    """
    A[i*3:i*3+3], A[j*3:j*3+3] = A[j*3:j*3+3], A[i*3:i*3+3]
    return A

def scale_row(A, row, scalar):
    """
    Multiplica un renglón de la matriz 3x3 representada como un array por un escalar.

    Parámetros:
    A (array): Array de 9 elementos de tipo flotante representando la matriz.
    row (int): Índice del renglón a escalar.
    scalar (float): El escalar por el cual multiplicar el renglón.

    Retorna:
    array: El array A con el renglón escalado.
    """
    for idx in range(row*3, row*3+3):
        A[idx] *= scalar
    return A

def add_multiple_of_row(A, source_row, destination_row, scalar):
    """
    Agrega un múltiplo de un renglón a otro renglón en una matriz 3x3 representada como un array.

    Parámetros:
    A (array): Array de 9 elementos de tipo flotante representando la matriz.
    source_row (int): Índice del renglón a multiplicar por el escalar.
    destination_row (int): Índice del renglón al que se le suma el múltiplo.
    scalar (float): El escalar por el cual multiplicar el renglón fuente.

    Retorna:
    array: El array A con la operación realizada.
    """
    for idx in range(3):
        A[destination_row*3+idx] += A[source_row*3+idx] * scalar
    return A


print(elem(f,1,2));
print(elem(f,2,2));

R=add_multiple_of_row(f,1,2,2);


"""Realizando las pruebas con symp"""

# se define en la matriz `A`

A = sp.Matrix([
    [1, 2, 3.14 ],
    [1, 0, 24],
    [0.9, 1999, 5]
])

A

print(R);




