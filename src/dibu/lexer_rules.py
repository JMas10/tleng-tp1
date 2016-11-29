tokens = [
   'NUM',
   'STRING',
   'ID',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'EQUALS',
   'NEWLINE'
   ]

def t_NUM(token):
    r"[0-9]+(\.[0-9]+)?"
    if token.value.find(".") >= 0:
        number_type = "float"
        number_value = float(token.value)
        number_line = token.lineno
        number_pos = token.lexpos
    else:
        number_type = "int"
        number_value = int(token.value)
        number_line = token.lineno
        number_pos = token.lexpos
    token.value = {"value": number_value, "type": number_type, "lineno": number_line, 'lexpos': number_pos}
    return token

def t_STRING(token):
    r"\"([a-zA-Z_+*-][a-zA-Z0-9_+*-]*)\""
    string_value = token.value[1:-1]
    string_line = token.lineno
    string_pos = token.lexpos
    token.value = {"value": string_value, "lineno": string_line, 'lexpos': string_pos}
    return token

def t_ID(token):
    r"[a-zA-Z_+*-][a-zA-Z0-9_+*-]*"
    string_value = str(token.value)
    string_line = token.lineno
    string_pos = token.lexpos
    token.value = {"value": string_value, "lineno": string_line, 'lexpos': string_pos}
    return token

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)
    return token

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_COMMA = r","
t_EQUALS = r"="

t_ignore = " \t"


def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
