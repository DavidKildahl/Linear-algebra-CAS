from sympy import *



# --- Matricer ---

A = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
#pprint(A)

# Definer søjlevektor
b = Matrix([7, 19, 31])
#pprint(b)

# Definer totalmatricer fra matrix og vektor
Ab = A.row_join(b)
#pprint(Ab)

# RREF
H = A.rref()
#pprint(H)

#pprint(Ab.rref())


# --- Matricer med symbolske indgange ---

# Definer variable/symboler, som vi kan arbejde med
a, b, c, d, e, f = symbols('a b c d e f')

B = Matrix([[a, b, e],
            [c, d, f]])

# Bemærk her antager SymPy at alle symbolske udtryk i nævnere er forskellige fra 0 
#pprint(B.rref())

# --- Beregn invers matrix ---

A = Matrix([[1, a, b],
            [0, 1, c],
            [0, 0, 1]])

#pprint(A.inv())

# --- Nulrum og søjlerum ---

A = Matrix([[2, 4],
            [1, 2]])

# Beregn udspændende vektorer for nulrummet
#pprint(A.nullspace())

# Beregn udspændende vektorer for søjlerummet
#pprint(A.columnspace())

A = Matrix([[1, 2, 3, 1, 1],
            [2, 3, 4, 3, 2],
            [3, 4, 5, 5, 4]])

#pprint(A.rref())
#pprint(A.columnspace())