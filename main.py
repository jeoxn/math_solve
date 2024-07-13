from PIL import Image
from pix2tex.cli import LatexOCR
from latex2sympy2 import latex2sympy, latex2latex
from sympy import *

def extract_variables(sympy_expr):   
    variables = sympy_expr.free_symbols
    variable_names = [str(variable) for variable in variables]

    return variable_names

FileName = "image.png"

img = Image.open(FileName)
model = LatexOCR()
tex = model(img)

tex = tex.replace("operatorname*{lim}", "lim")

try:
    sympy = latex2sympy(tex)
    variables = extract_variables(sympy)
    symbol = symbols(variables)

    soal = input("Masukkan hasil yang diinginkan: ")

    if soal == "turunan":
        solution = diff(sympy, symbol[0])
    elif soal == "integral":
        solution = integrate(sympy, symbol[0])
    elif soal == "selesaikan":
        solution = solve(sympy, symbol[0])
    elif soal == "sederhana":
        solution = simplify(sympy)
    elif soal == "faktor":
        solution = factor(sympy)
    elif soal == "ekspansi":
        solution = expand(sympy)
    elif soal == "pecah":
        solution = apart(sympy)
    else:
        solution = sympy.doit()
    
    pprint(solution)
except Exception as e:
    print(e)