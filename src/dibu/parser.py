import lexer_rules
import parser_rules

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc
from figuras import *


if __name__ == "__main__":
    if len(argv) != 3:
        print "Parametros invalidos."
        print "Uso:"
        print "  parser.py archivo_entrada nombre_imagen"
        exit()

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)
    try:
        scene = parser.parse(text, lexer)
        scene.nombre(argv[2])
        scene.write_svg()
        scene.display()
    except parser_rules.SemanticException as exception:
        print "Semantic error: " + str(exception)
    except parser_rules.SintacticException as exception:
        print str(exception)
    except lexer_rules.TokenException as exception:
        print str(exception)
