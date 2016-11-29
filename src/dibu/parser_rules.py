from lexer_rules import tokens
from helper import *

#TO DO: RESOLVER SIZE Y VER TEMA DE DICC PARAMS



idDicObligatory = {'rectangle': ['upper_left', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': ['points'], 'polygon':['points'],
                'text':['t', 'at']}

diccSize = {'height': [], 'width': []}
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

listaFiguras = []
# nuevoDicc = {}

def p_start(p):
    'start : program'
    scene = Scene('resultado')
    # if diccSize['height'].count > 1:
    #     print('Error - Dos sizes')
    # if diccSize['height'].count == 0:
    #     scene = Scene("resultado")
    # else:
    #     scene = Scene("resultado", diccSize['height'], diccSize['width'])
    for elem in listaFiguras:
        scene.add(elem)
    scene.write_svg()
    scene.display()

def p_program_nonempty(p):
    'program : state NEWLINE program'
    pass

def p_program_empty(p):
    'program : '
    pass

def p_state(p):
    'state : ID params'
    if p[1] == 'size':
        print('ver que hacer con size')
    else:
        params = p[2]['parametros']
        paramsOblig = idDicObligatory[p[1]]
        try:
            figura = inicializarFigura(p[1])
        except NameError:
            print('Figura Invalida - Finalizo la ejecucion')
        if incluido(paramsOblig, (params.keys())):
            for key,value in params.iteritems():
                try:
                    nombreMetodo = renombrar(key)
                    metodo = getattr(figura, nombreMetodo)
                    metodo(value)
                except AttributeError:
                    print('Parametro Invalido - Finalizo la ejecucion')

            listaFiguras.append(figura)
        else:
            print('Faltan Parametros obligatorios - Finalizo la ejecucion')

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'
    paramDicc = {}
    paramDicc.update({p[1]: p[3]})
    p[0] ={'parametros': paramDicc}

def p_params_recursive(p):
    'params : ID EQUALS valor COMMA params'
    if p[1] in p[5]['parametros']:
        #Error
        print('Error - Parametros repetidos')
    paramDicc = p[5]['parametros']
    paramDicc.update({p[1]: p[3]})
    p[0] = {'parametros': paramDicc}

def p_valor_number(p):
    'valor : NUM'
    p[0] = p[1]['value']

def p_valor_string(p):
    'valor : STRING'
    p[0] = p[1]

def p_valor_point(p):
    'valor : LPAREN NUM COMMA NUM RPAREN'
    p[0] = (p[2]['value'], p[4]['value'])

def p_valor_array(p):
    'valor : LBRACKET array RBRACKET'
    p[0] = p[2]

def p_array_element(p):
    'array : LPAREN NUM COMMA NUM RPAREN'
    p[0] = [(p[2]['value'], p[4]['value'])]

def p_array_recursive(p):
    'array : LPAREN NUM COMMA NUM RPAREN COMMA array'
    p[0] = [(p[2]['value'], p[4]['value'])] + p[7]

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
        if each not in l2:
            return False
    return True

def inicializarFigura(nombre):
    if nombre == 'rectangle':
        return Rectangle()
    elif nombre == 'line':
        return Line()
    elif nombre == 'circle':
        return Circle()
    elif nombre == 'ellipse':
        return Ellipse()
    elif nombre == 'polyline':
        return Polyline()
    elif nombre == 'polygon':
        return Polygon()
    elif nombre == 'text':
        return Text()
    else:
        raise NameError('algo')

def renombrar(nombre):
    #Tengo que renombrar metodos de Dibu porque algunos no son nombre validos de funciones en python
    if nombre == 'from':
        return 'from_'
    elif nombre == 'font-size':
        return 'font_size'
    elif nombre == 'font-family':
        return 'font_family'
    elif nombre == 'stroke-width':
        return 'stroke_width'
    else:
        return nombre
