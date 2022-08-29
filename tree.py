operator_list = ['+', '-', '*', '/', '(', ')', ' ', 'N']

operator_rank_table = {
    '+' : 1, '-' : 1, 
    '*' : 2, '/' : 2,
    '(' : 0,
    'N' : 9,
    ')' : 10
}

class node:
    def __init__(self) -> None:
        self.leftchild = None
        self.rightchild = None
        self.value = None
    def __str__(self) -> str:
        if self.leftchild and self.rightchild:
            if self.leftchild.value in operator_list and operator_rank_table[self.leftchild.value] < operator_rank_table[self.value]:
                left_str = '({})'.format(str(self.leftchild))
            else:
                left_str = str(self.leftchild)
            if self.rightchild.value in operator_list and operator_rank_table[self.rightchild.value] <= operator_rank_table[self.value]:
                right_str = '({})'.format(str(self.rightchild))
            else:
                right_str = str(self.rightchild)
            return left_str + str(self.value) + right_str
        else:
            return str(self.value)

def merge_tree(tree_left:node, tree_right:node, value) -> node:
    new_tree = node()
    new_tree.leftchild = tree_left
    new_tree.rightchild = tree_right
    new_tree.value = value
    return new_tree

