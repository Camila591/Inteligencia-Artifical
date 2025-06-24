"""
txt = "Hola mundo"
i = 0
while i < len(txt):
    print(txt[i])
    i +=1
"""
    #for x in txt:
    #  print(x)  

"""
num = int(input("ingrese el numero que desea multiplicar: "))
for x in range (0,11):
    mult = num * x
    print(f"{num} x {x} = {mult}")
"""
for x in range (1,11):
    for numero in range (1,11):
        print(x,"x",numero, "=", numero * x )
    print("")   