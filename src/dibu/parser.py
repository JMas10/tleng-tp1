import ply.yacc as yacc
from .lexer import tokens

# Build the parser
parser = yacc.yacc(debug=True)

def parse(str):
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
