keyword = {"break", "case", "continue", "default", "defer", "else", "for", 
"func", "goto", "if", "map", "range", "return", "struct", "type", "var"}

input_var = input()

if input_var in keyword:
    print(input_var, "is keyword")
else:
    print(input_var,"is mot keyword")