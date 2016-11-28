#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
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

tokens = [
   'NUMBER',
   'STRING',
   'ID',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'EQUALS'
]

def t_NUMBER(token):
    r"[0-9]+(\.[0-9]+)?"
    if token.value.find(".") >= 0:
        number_type = "float"
        number_value = float(token.value)
    else:
        number_type = "int"
        number_value = int(token.value)
    token.value = {"value": number_value, "type": number_type}
    return token

def t_STRING(token):
  r"\"([a-zA-Z_+=*-][a-zA-Z0-9_+*-]*)\""
  return token

def t_ID(token):
    r"[a-zA-Z_+=*-][a-zA-Z0-9_+*-]*"
    return token

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_COMMA = r","
t_EQUALS = r"="

t_ignore = " \t"


def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

# Build the lexer
lexer = lex.lex()

def apply(string):
    """Aplica el análisis léxico al string dado."""
    lex.input(string)

    return list(lexer)

# if __name__ == "__main__":
#     data = '''size height=200 width=200
#     rectangle upper_left=(0,0), size=(50, 50), fill="red"
#     rectangle upper_left=(100,0), size=(50, 50)
#     rectangle upper_left=(50,50), size=(50, 50)
#     rectangle upper_left=(150,50), size=(50, 50)
#     rectangle upper_left=(0,100), size=(50, 50)
#     rectangle upper_left=(100,100), size=(50, 50)
#     rectangle upper_left=(50,150), size=(50, 50)
#     rectangle upper_left=(150,150), size=(50, 50)'''
#
#     lexer = lex.lex()
#     print(apply(data))
#     print(lexer.lineno)
