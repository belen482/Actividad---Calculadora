
def sumar(a, b):
    resultado = a + b
    return resultado
print(sumar(5, 3))

def restar(a,b):
    return a - b
print(restar(5,3))

def multiplicar(a,b):
    multi = 0
    for i in range(b):
        multi = sumar(multi,a)
    return multi
print(multiplicar(5,3))
