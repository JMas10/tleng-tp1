from lexer import tokens

idDicObligatory = {'rectangle': ['upper_left', 'size'], 'line': ['from', 'to'],
                'circle':['center', 'radius'], 'ellipse':['center', 'rx', 'ry'], 'polyline': [], 'polygon':[],
                'text':['t', 'at']}

diccSize = dict.fromkeys(['height','width'])

listaFiguras = []

def p_start(p):
    'start : program'
    scene = Scene('resultado')
    if diccSize['height'].count > 1:
        print('Error - Dos sizes')
    if diccSize['height'].count == 0:
        scene = Scene("resultado")
    else:
        scene = Scene("resultado", diccSize['height'], diccSize['width'])

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
        try:
            figura = inicializarFigura(p[1])
        except NameError:
            print('Figura Invalida - Finalizo la ejecucion')
        if incluido(idDicObligatory[p[1]], params):
            for key,value in params:
                try:
                    metodo = getattr(figura, key)
                    metodo(value)
                except AttributeError:
                    print('Parametro Invalido - Finalizo la ejecucion')

            listaFiguras.append(figura)
        else:
            print('Faltan Parametros obligatorios - Finalizo la ejecucion')

def p_params_recursive(p):
    'params : ID EQUALS valor COMMA params'
    if p[1] in p[4]['parametros']:
        #Error
        print('error')
    p[0] = {'parametros':p[4]['parametros'].update(p[1], p[3])}

def p_params_nonrecursive(p):
    'params : ID EQUALS valor'
    p[0] ={'parametros':{p[1]: p[3]}}

def p_valor_number(p):
    'valor : NUMBER'
    p[0] = p[1]['value']

def p_valor_string(p):
    'valor : STRING'
    p[0] = p[1]

def p_valor_point(p):
    'valor : LPAREN NUMBER COMMA NUMBER RPAREN'
    p[0] = p[1] + str(p[2]['value']) + p[3] + str(p[4]['value']) + p[5]

def p_valor_array(p):
    'valor : LBRACKET array RBRACKET'
    p[0] = p[1] + p[2] + p[3]

def p_array_element(p):
    'array : valor'
    p[0] = p[1] + p[2]['value'] + p[3] + p[4]['value'] + p[5]

def p_array_recursive(p):
    'array : LPAREN NUMBER COMMA NUMBER RPAREN COMMA array'
    p[0] = p[1] + str(p[2]['value']) + p[3] + str(p[4]['value']) + p[5] + p[6] + p[7]

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
