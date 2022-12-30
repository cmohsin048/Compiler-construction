import ast
code = 'one_plus_two = 1+2 # type: int'
tree = ast.parse(code, type_comments=True)
print(ast.dump(tree))
