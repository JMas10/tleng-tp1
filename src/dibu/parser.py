import lexer_rules
import parser_rules

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":
    if len(argv) != 2:
        print "Parametros invalidos."
        print "Uso:"
        print "  parser.py archivo_entrada"
        exit()

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)

    ast = parser.parse(text, lexer)
