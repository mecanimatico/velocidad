list_impar = []
list_par = []
list = range(10)
for i in list:
    if i % 2 == 0:
        list_par.append(i)
    else:
        list_impar.append(i)


print(list_par)
print(list_impar)