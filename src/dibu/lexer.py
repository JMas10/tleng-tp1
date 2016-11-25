import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como quedarnos
con algún valor de ese elemento.

"""


tokens = (
)


def t_error(t):
    pass

# Build the lexer
lexer = lex.lex()

def apply(string):
    u"""Aplica el análisis léxico al string dado."""
    lex.input(string)

    return list(lexer)
