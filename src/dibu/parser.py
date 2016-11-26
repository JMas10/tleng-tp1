import ply.yacc as yacc
from .lexer import tokens

idDicObligatory = {'size': ['height', 'width'], 'rectangle': ['upper_left', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': [], 'polygon':[],
                'text':['t', 'at'], 'optional':['fill', 'stroke', 'stroke-width']}

diccSize = dict.fromkeys(['height','width'])
diccRect = dict.fromkeys(['origin','height','width','fill_color', 'line_color','line_width'])
diccLine = dict.fromkeys(['start','end','color','width'}
diccCircle = dict.fromkeys(['center','radius','fill_color','line_color','line_width'])
diccEllipse  = dict.fromkeys(['center','radius_x','radius_y','fill_color','line_color','line_width])
diccPolyline = dict.fromkeys(['points','fill_color','line_color','line_width'])
diccPolygon = dict.fromkeys(['points','fill_color','line_color','line_width'])
diccText = dict.fromkeys(['origin','text','size','color'])

diccFiguras= {'size': diccSize, 'rectangle': diccRect, 'line': diccLine,
                'circle':diccCircle, 'ellipse':diccEllipse, 'polyline': diccPolyline, 'polygon':diccPolygon,
                'text':diccText}


def p_start(p):
    'start : program'
    if diccFiguras['size']['height'].count > 1:
        #Error
    if diccFiguras['size']['height'].count == 0:
        scene = Scene("resultado")
    else:
        scene = Scene("resultado", diccFiguras['size']['height'], diccFiguras['size']['width'])

    diccFiguras.pop('size', None)
    for each in diccFiguras:
        for cada in diccFiguras[each]:
            if each == 'rectangle':

                scene.add(Rectangle((100,100),200,200,(0,255,255),(0,0,0),1))
            elif each == 'line':

            elif each == 'circle':

            elif each == 'ellipse':

            elif each == 'polyline':

            elif each == 'polygon':

            elif each == 'text':


    scene.add(Rectangle((100,100),200,200,(0,255,255),(0,0,0),1))
    scene.add(Line((200,200),(200,300),(0,0,0),1))
    scene.add(Line((200,200),(300,200),(0,0,0),1))

    scene.add(Text((50,50),"Testing SVG",24,(0,0,0)))
    scene.write_svg()
    scene.display()

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
        values = idDicObligatory[p[1]]
        params = p[2]['parametros']
        if incluido(params, values.extend(idDicObligatory["optional"]))) and incluido(values, params):
            for each in params:
                diccFiguras[p[1]][each].append(params[each])
        else:
            #error
    else:
        #error

def p_params_recursive(p):
    'params : ID EQUALS valor params'
    if p[1] in p[4]['parametros']:
        #Error
    p[0] ={'parametros':p[4]['parametros'].update(p[1], p[3]), 'value': p[1] + p[2] + p[3] + p[4]['value']}

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'
    p[0] ={'parametros':{p[1]: p[3]}} #No estamos seguros de la concatenacion.

def p_valor_number(p):
    'valor : NUM'
    p[0] = p[1]['value']

def p_valor_string(p):
    'valor : STRING'
    p[0] = p[1]

def p_valor_point(p):
    'valor : LPAREN NUM COMMA NUM RPAREN'
    p[0] = p[1] + p[2]['value'] + p[3] + p[4]['value'] + p[5]

def p_valor_array(p):
    'valor : LBRACKET array RBRACKET'
    p[0] = p[1] + p[2] + p[3]

def p_array_element(p):
    'array : LPAREN NUM COMMA NUM RPAREN'
    p[0] = p[1] + p[2]['value'] + p[3] + p[4]['value'] + p[5]

def p_array_recursive(p):
    'array : LPAREN NUM COMMA NUM RPAREN COMMA array'
    p[0] = p[1] + p[2]['value'] + p[3] + p[4]['value'] + p[5] + p[6] + p[7]

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

def incluido(l1, l2):
    for each in l1:
        if not each in l2:
            return false
    return true


# Build the parser
parser = yacc.yacc(debug=True)

def parse(str):
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
