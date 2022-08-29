import re
from tree import *

def _rpn2tree(notation:list) -> node:
    number_stack = []
    for symbol in notation:
        if symbol in operator_list:
            right_node = number_stack.pop()
            left_node = number_stack.pop()
            number_stack.append(merge_tree(left_node, right_node, symbol))
        else:
            new_node = node()
            new_node.value = symbol
            number_stack.append(new_node)
    return number_stack[0]

def _negative_number_process(notation:str) -> str:
    if notation[0] == '-':
        notation = '0N' + notation[1:]
    notation = notation.replace(' ','')
    notation = re.sub(r'([(+\-*/])-', r'\g<1>0N', notation)
    return notation


def _notation2list(notation: str) -> list:
    left, right = 0, 0
    symbol = []
    while right < len(notation):
        if notation[right] in operator_list:
            if left == right:
                if not notation[right] == ' ':
                    symbol.append(notation[left])
                left += 1
                right += 1
                continue
            try:
                num = int(notation[left:right])
            except:
                try:
                    num = float(notation[left:right])
                except:
                    raise Exception('illegal Expression')
            symbol.append(num)
            if not notation[right] == ' ':
                symbol.append(notation[right])
            right += 1
            left = right
        else:
            right += 1
    if left >= len(notation):
        pass
    else:
        try:
            num = int(notation[left:])
        except:
            try:
                num = float(notation[left:])
            except:
                raise Exception('illegal Expression')
        symbol.append(num)
    return symbol


def _value_of_pn(notation: list) -> float:
    operator_number = []
    while len(notation):
        symbol = notation.pop()
        if symbol in operator_list:
            try:
                if symbol in ['(', ')', ' ']:
                    continue
                elif symbol == '+':
                    operator_number.append(operator_number.pop() + operator_number.pop())
                elif symbol in ['-', 'N']:
                    operator_number.append(operator_number.pop() - operator_number.pop())
                elif symbol == '*':
                    operator_number.append(operator_number.pop() * operator_number.pop())
                elif symbol == '/':
                    operator_number.append(operator_number.pop() / operator_number.pop())
                else:
                    pass
            except:
                raise Exception('illegal Expression')
        else:
            operator_number.append(symbol)
    return operator_number[0]

def _value_of_rpn(notation: list) -> float:
    operator_number = []
    while len(notation):
        symbol = notation.pop(0)
        if symbol in operator_list:
            try:
                if symbol in ['(', ')', ' ']:
                    continue
                elif symbol == '+':
                    operator_number.append(operator_number.pop() + operator_number.pop())
                elif symbol in ['-', 'N']:
                    operator_number.append(- operator_number.pop() + operator_number.pop())
                elif symbol == '*':
                    operator_number.append(operator_number.pop() * operator_number.pop())
                elif symbol == '/':
                    t = operator_number.pop()
                    operator_number.append(operator_number.pop() / t)
            except:
                raise Exception('illegal Expression')
        else:
            operator_number.append(symbol)
    return operator_number[0]

def _infix2rpn(notation: list) -> list:
    number_stack = []
    operator_stack = []
    for symbol in notation:
        if symbol in operator_list:
            if symbol == '(' or not operator_stack:
                operator_stack.append(symbol)
            elif symbol == ')':
                while True:
                    t = operator_stack.pop()
                    if t == '(':
                        break
                    number_stack.append(t)
            else:
                while operator_stack and operator_rank_table[symbol] <= operator_rank_table[operator_stack[-1]]:
                    number_stack.append(operator_stack.pop())
                operator_stack.append(symbol)
        else:
            number_stack.append(symbol)
    while operator_stack:
        number_stack.append(operator_stack.pop())
    return number_stack

def get_value_of_infix(experssion:str) -> float:
    return _value_of_rpn(_infix2rpn(_notation2list(_negative_number_process(experssion))))

def get_value_of_pn(experssion:str) -> float:
    return _value_of_pn(_notation2list(experssion))

def get_value_of_rpn(experssion:str) -> float:
    return _value_of_pn(_notation2list(experssion))

def infix2rpn(experssion:str) -> str:
    symbol_list = _infix2rpn(_notation2list(_negative_number_process(experssion)))
    rpn = ''
    for symbol in symbol_list:
        rpn += (str(symbol) + ' ')
    rpn = rpn.replace('N', '-')
    return rpn

def rpn2infix(experssion:str) -> str:
    symbol_list =_notation2list(experssion)
    tree = _rpn2tree(symbol_list)
    infix = str(tree)
    infix = infix.replace('0-', '-')
    return infix

def remove_parentheses(experssion:str) -> str:
    return rpn2infix(infix2rpn(experssion))

# print(remove_parentheses('(-3*-4)+((6+5)*2)'))