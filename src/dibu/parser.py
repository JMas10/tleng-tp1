#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lexer
import parser_rules

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc

from helper import *

#TO DO: PROBAR FUNCIONALIDAD

# diccRect = dict.fromkeys(['origin','height','width','fill_color', 'line_color','line_width'])
# diccLine = dict.fromkeys(['start','end','color','width'}
# diccCircle = dict.fromkeys(['center','radius','fill_color','line_color','line_width'])
# diccEllipse  = dict.fromkeys(['center','radius_x','radius_y','fill_color','line_color','line_width])
# diccPolyline = dict.fromkeys(['points','fill_color','line_color','line_width'])
# diccPolygon = dict.fromkeys(['points','fill_color','line_color','line_width'])
# diccText = dict.fromkeys(['origin','text','size','color'])
#
# diccFiguras= {'size': diccSize, 'rectangle': diccRect, 'line': diccLine,
#                 'circle':diccCircle, 'ellipse':diccEllipse, 'polyline': diccPolyline, 'polygon':diccPolygon,
#                 'text':diccText}


def parse(str):
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
	
# Build the parser	
if __name__ == "__main__":
    if len(argv) == 0:
        print "Parametros invalidos."
        print "Uso:"
        print "  parser.py archivo_entrada archivo_salida"
        exit()

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer)
    parser = yacc(module=parser_rules)

    ast = parser.parse(text, lexer)

    output_file = open(argv[2], "w")
    dump_ast(ast, output_file)
    output_file.close()
