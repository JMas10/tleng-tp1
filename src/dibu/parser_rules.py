from lexer_rules import tokens
from figuras import *


class SemanticException(Exception):
    pass

class SintacticException(Exception):
    pass

idDicObligatory = {'rectangle': ['upper_left', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': ['points'], 'polygon':['points'],
                'text':['t', 'at']}

diccSize = {'height': [], 'width': [], 'lineno': [], 'lexpos': []}

listaFiguras = []

def p_start(p):
    'start : program'
    scene = Scene('imagen')
    cantidadSize = len(diccSize['height'])
    if cantidadSize > 1:
        raise SemanticException("Dos o Mas Size " + "\nline: " + str(diccSize["lineno"][1]) + "\nposition: " + str(diccSize["lexpos"][1]))
    if cantidadSize == 0:
        scene = Scene("imagen")
    else:
        height = diccSize['height'][0]
        width = diccSize['width'][0]
        scene = Scene("imagen", height, width)
    for elem in listaFiguras:
        scene.add(elem)
    p[0] = scene

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
    else:
        params = p[2]['parametros']
        try:
            paramsOblig = idDicObligatory[p[1]["value"]]
            figura = inicializarFigura(p[1]["value"])
        except KeyError:
            # Error figura invalida
            raise SemanticException("Figura Invalida " + "\nline: " + str(p[2]["lineno"])+ "\nposition: " + str(p[2]["lexpos"]))
        if incluido(paramsOblig, (params.keys())):
            for key,value in params.iteritems():
                try:
                    nombreMetodo = renombrar(key)
                    metodo = getattr(figura, nombreMetodo)
                    metodo(value)
                except AttributeError:
                    # Error parametro invalido
                    raise SemanticException("Parametro Invalido " + "\nline: " + str(p[2]["lineno"])+ "\nposition: " + str(p[2]["lexpos"]))

            listaFiguras.append(figura)
        else:
            # Error faltan parametros obligatorios
            raise SemanticException("Faltan Parametros obligatorios " + "\nline: " + str(p[2]["lineno"])+ "\nposition: " + str(p[2]["lexpos"]))

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'
    paramDicc = {}
    paramDicc.update({p[1]["value"]: p[3]["value"]})
    p[0] = {'parametros': paramDicc, "lineno": p[1]["lineno"], "lexpos": p[1]["lexpos"]}

def p_params_recursive(p):
    'params : ID EQUALS valor COMMA params'
    if p[1]["value"] in p[5]['parametros']:
        #Error Parametros repetidos
        raise SemanticException('Parametros repetidos ' + "\nline: " + str(p[1]["lineno"])+ "\nposition: " + str(p[1]["lexpos"]))
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
    message = "Syntax error"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise SintacticException(message)

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
