txt = open("calorias.txt", "r")

calorias = txt.read()

lista_calorias = calorias.split("\n\n")

lista = []
maior_cal = 0
i = 0

txt.close()

for numbers in lista_calorias:
    lista.append(numbers.split("\n"))


lista_int = [[int(x) for x in y] for y in lista]

for item in lista_int:
    if maior_cal < sum(item):
        maior_cal = sum(item)
        
for item in lista_int:
    if maior_cal == sum(item):
        i = lista_int.index(item)

print(f"o indice do elfo com o maior numero de calorias é {i}") 
print(f"o maior número de calorias foi {maior_cal}")

#PART 2


lista_sum = []
top_calorias = []

for item in lista_int:
    lista_sum.append(sum(item))

lista_sum.sort()
top_calorias = lista_sum[-3:]

top_calorias_sum = sum(top_calorias)

print(f"O total carregado pelos elfos com maior numero de calorias é {top_calorias_sum}")
