import ply.yacc as yacc
from .lexer import tokens

idDicObligatory = {'size': ['height', 'width'], 'rectangle': ['height', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': [], 'polygon':[],
                'text':['t', 'at']}

def p_start(p):
    'start : program'

def p_program_nonempty(p):
    'program : state NEWLINE program'

def p_program_empty(p):
    'program : '
    pass

def p_state(p):
    'state : ID params'
    if p[1] in idDicObligatory:
        # Tengo que chequear: parametros obligatorios, sin repetir
        # Que size sea llamado una sola vez
    else:
        #error

def p_params_recursive(p):
    'params : ID EQUALS valor params'

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'

def p_valor_number(p):
    'valor : NUM'
    p[0] = p[1]

def p_valor_string(p):
    'valor : STRING'
    p[0] = p[1]

def p_valor_point(p):
    'valor : LPAREN NUM COMMA NUM RPAREN'

def p_valor_array(p):
    'valor : LBRACKET array RBRACKET'

def p_array_element(p):
    'array : LPAREN NUM COMMA NUM RPAREN'

def p_array_recursive(p):
    'array : LPAREN NUM COMMA NUM RPAREN COMMA array'

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

# Build the parser
parser = yacc.yacc(debug=True)

def parse(str):
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
