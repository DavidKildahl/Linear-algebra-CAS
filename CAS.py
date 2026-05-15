from sympy import *
from copy import deepcopy



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

A = Matrix([[0, 6, 6, 3],
            [1, 2, 1, 1],
            [4, 1, -3, 4]])

#pprint(A.rref())

# Beregn udspændende vektorer for nulrummet
#pprint(A.nullspace())

# Beregn udspændende vektorer for søjlerummet
#pprint(A.columnspace())

# Beregn udspændende vektorer for rækkerummet
#pprint(A.rowspace())

# --- Gram-Schmidt ---

# Følgende kode anvender Gram-Schmidt-processen på en basis af vektorer

def inner_product(u, v, coeff):
    return sum(coeff[i] * u[i] * v[i] for i in range(len(u)))

def gram_schmidt(V, coeff):
    m, n = shape(V)
    # Initialiser matrix. Søjler skal udgøre den ortonormale basis
    U = zeros(m, n)

    # Lav også matrix til projektionerne undervejs
    P = zeros(m, n - 1)
    
    for i in range(n):
        u = deepcopy(V[:, i]) # Undgå at ændre i oprindelige matrix

        # Hvis i > 0, skal vi beregne en projektion
        if i > 0:
            #print(f"{i = }")
            p = zeros(m, 1)
            for j in range(i):
                #print(inner_product(u, U[:, j], coeff))
                p += inner_product(u, U[:, j], coeff) * U[:, j]
            
            P[:, i - 1] = p
            u -= p
        
        # Normaliser
        u /= (sqrt(inner_product(u, u, coeff)))

        # Indsæt 
        U[:, i] = u
    
    return U, P

# Eksempel: Opgave 1, eksamen S19

# V matrix med vektorer som søjler
V = Matrix([[1, 5, 4], 
            [0, 1, -1], 
            [1, 1, 0]])

# Koefficienter til det indre produkt
coeff = (1, 1, 1)

#pprint(V)
U, P = gram_schmidt(V, coeff)
#pprint(U)
#pprint(P)

# --- Egenværdier ---

A = Matrix([[1, 0, -1], # Eksempel fra aflevering 9
            [2, 2, 2],
            [-1, 0, 1]])

#pprint(A)

# Bestem det karakteristiske polynomium, bemærk her det(lambda*I - A), så vi risikerer omvendt fortegn
pA = A.charpoly()
#pprint(pA)
#pprint(factor(pA.as_expr())) # Faktoriser

# Bestem egenværdier med algebraisk multiplicitet
#pprint(A.eigenvals())

# Bestem basis for egenrum og geometrisk multiplicitet
#pprint(A.eigenvects())

# --- Integration ---

t = symbols('t')
# Integrate cos(t)*sin(t) on the interval [0, pi]
#pprint(integrate(cos(t) * sin(t), (t, 0, pi)))