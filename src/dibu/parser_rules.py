from lexer_rules import tokens
from helper import *

#TO DO: RESOLVER SIZE Y VER TEMA DE DICC PARAMS

class SemanticException(Exception):
    pass

idDicObligatory = {'rectangle': ['upper_left', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': ['points'], 'polygon':['points'],
                'text':['t', 'at']}

diccSize = {'height': [], 'width': [], 'lineno': [], 'lexpos': []}
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
    cantidadSize = len(diccSize['height'])
    print(cantidadSize)
    if cantidadSize > 1:
        raise SemanticException("Dos o Mas Size " + "Linea " + str(diccSize["lineno"][1]) + " Posicion " + str(diccSize["lexpos"][1]))
    if cantidadSize == 0:
        scene = Scene("resultado")
    else:
        height = diccSize['height'][0]
        width = diccSize['width'][0]
        scene = Scene("resultado", height, width)
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
    if p[1]["value"] == 'size':
        params = p[2]['parametros']
        line = p[1]['lineno']
        pos = p[1]['lexpos']
        paramsOblig = ["height", "width"]
        if incluido(paramsOblig, (params.keys())):
            for key,value in params.iteritems():
                diccSize[key] = diccSize[key] + [value]
        diccSize["lineno"] = diccSize["lineno"] + [line]
        diccSize["lexpos"] = diccSize["lexpos"] + [pos]
        print(diccSize)
    else:
        params = p[2]['parametros']
        try:
            paramsOblig = idDicObligatory[p[1]["value"]]
            figura = inicializarFigura(p[1]["value"])
        except KeyError:
            # Error figura invalida
            raise SemanticException("Figura Invalida " + "Linea" + str(p[2]["lineno"])+ " Posicion " + str(p[2]["lexpos"]))
        if incluido(paramsOblig, (params.keys())):
            for key,value in params.iteritems():
                try:
                    nombreMetodo = renombrar(key)
                    metodo = getattr(figura, nombreMetodo)
                    metodo(value)
                except AttributeError:
                    # Error parametro invalido
                    raise SemanticException("Parametro Invalido " + "Linea" + str(p[2]["lineno"])+ " Posicion " + str(p[2]["lexpos"]))

            listaFiguras.append(figura)
        else:
            # Error faltan parametros obligatorios
            raise SemanticException("Faltan Parametros obligatorios " + "Linea" + str(p[2]["lineno"])+ " Posicion " + str(p[2]["lexpos"]))

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'
    paramDicc = {}
    paramDicc.update({p[1]["value"]: p[3]["value"]})
    p[0] = {'parametros': paramDicc, "lineno": p[1]["lineno"], "lexpos": p[1]["lexpos"]}

def p_params_recursive(p):
    'params : ID EQUALS valor COMMA params'
    if p[1]["value"] in p[5]['parametros']:
        #Error Parametros repetidos
        raise SemanticException('Parametros repetidos ' + "Linea" + str(p[1]["lineno"])+ " Posicion " + str(p[1]["lexpos"]))
    paramDicc = p[5]['parametros']
    paramDicc.update({p[1]["value"]: p[3]["value"]})
    p[0] = {'parametros': paramDicc, "lineno": p[1]["lineno"], "lexpos": p[1]["lexpos"]}

def p_valor_number(p):
    'valor : NUM'
    p[0] = p[1]

def p_valor_string(p):
    'valor : STRING'
    p[0] = p[1]

def p_valor_point(p):
    'valor : LPAREN NUM COMMA NUM RPAREN'
    p[0] = {"value": (p[2]['value'], p[4]['value']), "lineno": p[2]["lineno"], "lexpos": p[2]["lexpos"]}

def p_valor_array(p):
    'valor : LBRACKET array RBRACKET'
    p[0] = {'value':p[2]['value'], 'lineno':p[2]['lineno'], 'lexpos' :p[2]['lexpos']}

def p_array_element(p):
    'array : LPAREN NUM COMMA NUM RPAREN'
    p[0] = {"value": [(p[2]['value'], p[4]['value'])], "lineno": p[2]["lineno"], "lexpos": p[2]["lexpos"]}

def p_array_recursive(p):
    'array : LPAREN NUM COMMA NUM RPAREN COMMA array'
    value = [(p[2]['value'], p[4]['value'])] + p[7]
    p[0] = {"value": value, "lineno": p[2]["lineno"], "lexpos": p[2]["lexpos"]}

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

# def semantic_error(tipo, line, position):
#     message = "[Semantic error]"
#     last_cr = text.rfind('\n',0,position)
#     if last_cr < 0:
# 	       last_cr = 0
#     column = (position - last_cr) + 1
#     message += "\ntipo:" + tipo
#     message += "\nlinea:" + str(line)
#     message += "\nposicion:" + str(column)
#     raise Exception(message)

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
        raise KeyError('algo')

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
