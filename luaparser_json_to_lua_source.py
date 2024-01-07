KEY_LOCK = 'ALREADY_LOAD'

def json_to_lua_source(ast)
    def visit(dex):
        source = ''
        if isinstance(dex,dict):
            for key,item in dex.items():
                if key == 'Name' and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += str((item.get("id")))
                if (key == "LocalAssign" or key == "Assign") and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    start  = 'local'
                    if key == "Assign":
                        start = ''
                    coutitem = 0
                    for i,v in enumerate(item.get('targets')):
                        Id = visit(v)
                        source += start + f' {Id} = ' + visit(item.get('values')[i]) + ';'
                if key == 'Table' and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '{'

                    try:
                        for field in item['fields']:
                         source += visit(field) + ','
                    except:
                        pass
                    
                    source += "}"
                
                if key == 'Field' and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    KeyTable = visit(item.get('key'))
                    value = visit(item.get('value'))
                    source += '[' + str(KeyTable) + '] = ' + value + ''
                if key == 'Number' and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += str(item.get('n') or 0)
                if key == "Nil" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'nil'
                if key == "TrueExpr" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'true'
                if key == "FalseExpr" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'false'
                if key == "String" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    value = item['s']
                    if '\n' in value:
                        source += f'[[{value}]]'
                    elif '"' in value:
                        source += f"'{value}'"
                    else:
                        source += f'"{value}"'
                if key == "Dots" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '...'
                if key == "AnonymousFunction" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += "function("
                    source += (item.get('args') and visit(item.get('args'))) or ""
                    source += ")\n"
                    source += visit(item.get('body'))
                    source += '\n end;'
                if (key == "AddOp") and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '+' + str(visit(item.get('right'))) + ')'
                if key == "SubOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '-' + str(visit(item.get('right'))) + ')'
                if key == "MultOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '*' + str(visit(item.get('right'))) + ')'
                if key == "FloatDivOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '/' + str(visit(item.get('right'))) + ')'
                if key == "FloorDivOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '//' + str(visit(item.get('right'))) + ')'
                if key == "ModOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '%' + str(visit(item.get('right'))) + ')'
                if key == "ExpoOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '^' + str(visit(item.get('right'))) + ')'
                if key == "BAndOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '&' + str(visit(item.get('right'))) + ')'
                if key == "BOrOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '|' + str(visit(item.get('right'))) + ')'
                if key == "BShiftROp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '>>' + str(visit(item.get('right'))) + ')'
                if key == "BXorOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '~' + str(visit(item.get('right'))) + ')'
                if key == "BShiftLOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '<<' + str(visit(item.get('right'))) + ')'
                if (key == "LessThanOp" or key == "RLtOp") and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '<' + str(visit(item.get('right'))) + ')'
                if key == "GreaterThanOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '>' + str(visit(item.get('right'))) + ')'
                if key == "LessOrEqThanOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '<=' + str(visit(item.get('right'))) + ')'
                if key == "GreaterOrEqThanOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '>=' + str(visit(item.get('right'))) + ')'
                if (key == "EqToOp" or  key == 'REqOp') and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '==' + str(visit(item.get('right'))) + ')'
                if key == "NotEqToOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + str(visit(item.get('left'))) + '~=' + str(visit(item.get('right'))) + ')'
                if key == "NotEqToOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + '(' + str(visit(item.get('left'))) + ')' + 'and' + '(' + str(visit(item.get('right'))) + ')' + ')'
                if (key == "OrLoOp" or key == "LOrOp" )and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + '(' + str(visit(item.get('left'))) + ')' + 'or' + '(' + str(visit(item.get('right'))) + ')' + ')'
                if key == "Concat" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source +='(' + '(' + str(visit(item.get('left'))) + ')' + '..' + '(' + str(visit(item.get('right'))) + ')' + ')'
                if key == "UMinusOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '-' + visit(item.get('operand') or None)
                if key == "UBNotOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '~' + visit(item.get('operand') or None)
                if key == "ULNotOp" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'not ' + visit(item.get('operand') or None)
                if key == "ULengthOP" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '#' + visit(item.get('operand') or None)
                if key == "Index" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    idx = item.get('idx')
                    if idx.get('String'):
                        source += visit(item['value']) + '[' + visit(idx) + ']'
                    elif idx.get('Name'):
                        source += visit(item['value']) + '.' + visit(idx) + ''
                    else:
                        source += visit(item['value']) + '[' + visit(idx) + ']'
                if key == "Varargs" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'repeat\n' + visit(item.get('body')) + '\nuntil ' + visit(item.get('test'))
                if key == "Method" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'function ' + visit(item['source']) + ':' + visit(item['name']) + '(' + visit(item.get('args')) + ')' + visit(item.get('body')) + '\nend;'
            
                if key == "LocalFunction" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'local function ' + visit(item['name']) + f'({visit(item.get("args"))})\n' + visit(item.get('body')) + '\nend;'

                if key == "Function" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'function ' + visit(item['name']) + f'({visit(item.get("args"))})\n' + visit(item.get('body')) + '\nend;'
                if key == "Invoke" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += visit(item.get('source')) + ':' + visit(item.get('func')) + f'({visit(item.get("args"))})'
                if key == "Call" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += visit(item.get('func')) + f'({visit(item.get("args"))})'
                if key == "Forin" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += " ".join(
                        ["for ", ",".join([visit(de) for de in item.get('targets')]), " in ", visit(item.get('iter')), " do\n"]
                    )
                    source += '\n' + visit(item.get('body')) + "\nend;"
                if key == "Fornum" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source = " ".join(
                    [
                        "for",
                        visit(item.get('target')),
                        "=",
                        ", ".join([visit(item.get('start')), visit(item.get('stop'))]),
                    ]
                    )
                    if item.get('step') > 1:
                        source += ", " + visit(item.get('step'))
                    source += " do\n" + visit(item.get('body')) + "\nend;"
                if key == "Return" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    val = visit(item.get('values'))
                    if val == 'False':
                        source += 'return '
                    else:
                        source += 'return ' + val
                if key == "Break" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'break'
                if key == "Goto" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += 'goto ' + visit(item.get('label'))
                if key == "Label" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += '::' + visit(item.get('id')) + '::'
                if key == "If" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source = (
                        "if " + visit(item.get('test')) + " then\n" + visit(item.get('body'))
                    )
                    if item.get('orelse'):
                        source += visit(item.get("orelse")) + "\nelse\n"
                    source += "\nend;"
                if key == "ElseIf" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += (
                            "elseif " + visit(item.get('test')) + " then\n" + visit(item.get('body'))
                    )
                    if item.get('orelse'):
                        source += "\n" + visit(item.get("orelse"))
                if key == "Do" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source + 'do\n' + visit(item.get('body')) + '\nend;'
                if key == "While" and not item.get(KEY_LOCK):
                    item[KEY_LOCK] = 'true'
                    source += "while " + visit(item.get('test')) + " do\n" + visit(item.get('body')) + "\nend;"
                source += visit(item)

        elif isinstance(dex,list):
            source += " ".join([visit(n) for n in dex])
        return source
    return visit(ast)
