def funcao(x):
    return x ** 2
inicio = 0
fim = 1
delta = 0.5
areazona = 0
while inicio < fim:
    altura = funcao(inicio)
    base = delta
    areazinha = base * altura
    areazona += areazona
    inicio += delta
print(areazona)

